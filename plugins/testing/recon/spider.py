#!/usr/bin/env python
# -*- coding: utf-8 -*-


from golismero.api.config import Config
from golismero.api.data.information.html import HTML
from golismero.api.data.information.text import Text
from golismero.api.data.resource.email import Email
from golismero.api.data.resource.url import URL, BaseURL, SpiderURL, FolderURL
from golismero.api.logger import Logger
from golismero.api.net import NetworkException
from golismero.api.net.scraper import extract_from_html, extract_from_text, extract_forms_from_html
from golismero.api.net.web_utils import download, parse_url, argument_query
from golismero.api.plugin import TestingPlugin
from golismero.api.text.wordlist import WordListLoader

from traceback import format_exc
from warnings import warn

from wvs_spider.run import start_wvs_spider_dispatch
import json

#------------------------------------------------------------------------------
class Spider(TestingPlugin):
    """
    This plugin is a web spider.
    """


    #--------------------------------------------------------------------------
    def get_accepted_types(self):
        return [SpiderURL]


    #--------------------------------------------------------------------------
    def run(self, info):

        m_return = []

        m_url = info.url

        __ = start_wvs_spider_dispatch(m_url, Logger)
        json_content = json.loads(__)

        for urls in json_content['info']:
            #print item
            Logger.log_verbose("Web Spider:found url %s" % urls['fullurl'])
            m_resource = URL(url = urls['fullurl'])
            m_return.append(m_resource)
            for item_url in urls['content']:
                post_param = item_url['param_data']
                if "AcunetixBoundary_" in post_param:  #multipart/form-data
                    method = 'FILE_UPLOAD'
                else:
                    method = item_url['method']

                if method == "POST":
                    post_param_dict = argument_query(item_url['param_data'])
                    m_resource = URL(url = item_url['url'], method = "POST", post_params = post_param_dict, referer= urls['fullurl'])
                else:
                    m_resource = URL(url = item_url['url'], method = method,  referer = urls['fullurl'])
                Logger.log_verbose("Web Spider:found url %s" % item_url['url'])
                m_return.append(m_resource)

        # Send the results
        return m_return


