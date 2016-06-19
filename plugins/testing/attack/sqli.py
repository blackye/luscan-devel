#!/usr/bin/env python
# -*- coding: utf-8 -*-


from golismero.api.config import Config
from golismero.api.data.information.html import HTML
from golismero.api.data.information.text import Text
from golismero.api.data.resource.email import Email
from golismero.api.parallel import pmap
from golismero.api.data.resource.url import URL
from golismero.api.logger import Logger
from golismero.api.net import NetworkException
from golismero.api.net.scraper import extract_from_html, extract_from_text, extract_forms_from_html
from golismero.api.net.web_utils import download, parse_url, argument_query, download
from golismero.api.plugin import TestingPlugin
from golismero.api.text.wordlist import WordListLoader
from golismero.api.text.text_utils import to_utf8

from traceback import format_exc
from warnings import warn

from urllib import quote, quote_plus, unquote, unquote_plus
from scan_policy import sql_inject_detect_err_msg_test_cases
try:
    import re2 as re
except ImportError:
    import re
else:
    re.set_fallback_notification(re.FALLBACK_WARNING)

#------------------------------------------------------------------------------
class SqliPlugin(TestingPlugin):
    """
    This plugin is a web spider.
    """


    #--------------------------------------------------------------------------
    def get_accepted_types(self):
        return [URL]


    #--------------------------------------------------------------------------
    def run(self, info):
        #if not info.has_url_params and not info.has_post_params:
        #    return

        m_url = info.url
        m_url_parts = info.parsed_url

        # If file is a javascript, css or image, do not run
        if info.parsed_url.extension[1:] in ('css', 'js', 'jpeg', 'jpg', 'png', 'gif', 'svg', 'txt') or not m_url_parts.extension:
            Logger.log_more_verbose("Skipping URL: %s" % m_url)
            return

        m_return = []

        m_url = info.url

        if info.has_url_params:
            print '------'
            print 'get'
            print info.url, info.url_params
            for k,v in info.url_params.iteritems():
                key = to_utf8(k)
                value = to_utf8(v)
                for test_case_dict in sql_inject_detect_err_msg_test_cases:
                    info.url_params[key] = value + test_case_dict['input']
                    url_data = '&'.join(
                    '%s=%s' % ( quote(k, safe=''), quote(v, safe='') )
                    for (k, v) in sorted(info.url_params.iteritems())
                    )
                    __ = parse_url(info.url)
                    uri = __.scheme + '://' + __.host + ":" + str(__.port) + __.path + "?" + url_data
                    m_resource_url_payload = URL(url = uri, method = 'GET', referer = info.referer)
                    self.__get_request(m_resource_url_payload, test_case_dict['target'])
            print '******'

        if info.has_post_params:
            print 'POST'
            print info.url, info.post_params



        # Send the results
        return m_return

    def request_payload(self, url, get_param, post_param, method = 'GET'):
        pass

    def __get_request(self, url, test_case_re):
        print url
        try:
            p = download(url, None,
                         allow_redirects=False)

            print '*******'
            print url.url_params
            __ = re.search(test_case_re, p.raw_data)
            if __ is not None:
                print '[+] find sql inject in url {0}, param {1}'.format(url.url, url.url_params)
        except NetworkException, e:
            Logger.log_error_verbose("Error while processing %r: %s" % (url, str(e)))
            return None


     #--------------------------------------------------------------------------
    def check_download(self, url, name, content_length, content_type):
        print '******************'
        print url
        print name
        print content_length
        print content_type
