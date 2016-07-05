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

from scan_policy import cmd_inject_detect_test_cases

try:
    import re2 as re
except ImportError:
    import re
else:
    re.set_fallback_notification(re.FALLBACK_WARNING)

class CmdInjectPlugin(TestingPlugin):

    '''
    this plugin is a any file read plugin
    '''

    #--------------------------------------------------------------------------
    def get_accepted_types(self):
        return [URL]


    #--------------------------------------------------------------------------
    def run(self, info):

        m_return = []

        if info.has_url_params:
            #param_dict = info.url_params
            for k,v in info.url_params.iteritems():
                key = to_utf8(k)
                value = to_utf8(v)

                for cmd_inject_case in cmd_inject_detect_test_cases:
                    p = payload_muntants(info, payload = {'k': k , 'pos': 1, 'payload':cmd_inject_case['input'], 'type': 0}, bmethod = info.method, timeout = 15.0)

                    if cmd_inject_case['target'] is not None:
                        if p is not None:
                            __ = re.search(cmd_inject_case['target'], p.data)
                            if __ is not None:
                                Logger.log_verbose( '[+] found cmd inject!' )
                                return m_return



        if info.has_post_params:
            #param_dict = info.post_params
            for k,v in info.post_params.iteritems():
                key = to_utf8(k)
                value = to_utf8(v)

                for cmd_inject_case in cmd_inject_detect_test_cases:
                    p = payload_muntants(info, payload = {'k': k , 'pos': 1, 'payload':cmd_inject_case['input'], 'type': 0}, bmethod = info.method, timeout = 15.0)

                    if cmd_inject_case['target'] is not None:
                        if p is not None:
                            __ = re.search(cmd_inject_case['target'], p.data)
                            if __ is not None:
                                Logger.log_verbose( '[+] found cmd inject!' )
                                return m_return

        # Send the results
        return m_return





