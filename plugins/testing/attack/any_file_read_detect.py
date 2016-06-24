#!/usr/bin/env/python
#-*- coding:utf-8 -*-

__author__ = 'BlackYe.'

from golismero.api.config import Config
from golismero.api.data.information.html import HTML
from golismero.api.data.information.text import Text
from golismero.api.data.resource.email import Email
from golismero.api.parallel import pmap
from golismero.api.data.resource.url import URL
from golismero.api.logger import Logger
from golismero.api.net import NetworkException
from golismero.api.net.scraper import extract_from_html, extract_from_text, extract_forms_from_html
from golismero.api.net.web_utils import download, parse_url, argument_query, download, get_request
from golismero.api.plugin import TestingPlugin
from golismero.api.text.wordlist import WordListLoader
from golismero.api.text.text_utils import to_utf8
from golismero.api.net.web_mutants import payload_muntants

from scan_policy import any_file_read_detect_test_cases

try:
    import re2 as re
except ImportError:
    import re
else:
    re.set_fallback_notification(re.FALLBACK_WARNING)


class AnyFileReadPlugin(TestingPlugin):

    '''
    this plugin is a any file read plugin
    '''

    #--------------------------------------------------------------------------
    def get_accepted_types(self):
        return [URL]


    #--------------------------------------------------------------------------
    def run(self, info):
        #if not info.has_url_params and not info.has_post_params:
        #    return

        m_return = []

        if info.has_url_params:

            cookie_dict = Config.audit_config.cookie
            print cookie_dict
            if hasattr(cookie_dict, "iteritems"):
                    cookie_params = {
                        to_utf8(k): to_utf8(v) for k, v in cookie_dict.iteritems()
                    }
                    cookie_param = ';'.join(
                        '%s=%s' % (k ,v) for (k, v) in sorted(cookie_params.iteritems())
                    )

            print cookie_param
            print "GET"

            '''
            param_dict = info.url_params
            for k,v in param_dict.iteritems():

                key = to_utf8(k)
                value = to_utf8(v)

                for any_file_read_case in any_file_read_detect_test_cases:
                    p = payload_muntants(info, payload = {'k': k , 'pos': 1, 'payload':any_file_read_case['input'], 'type': 1}, bmethod = info.method)
                    __ = re.search(any_file_read_case['target'], p.data)
                    if __ is not None:
                        print '[+] found any file read!'
                        return m_return
            '''

        if info.has_post_params:
            print 'POST'

        # Send the results
        return m_return
