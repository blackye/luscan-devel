#!/usr/bin/env/python
#-*- coding:utf-8 -*-

"""
Web muntants API.

Package payload to URL request, and Get Response info data from payload requests
"""

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
from golismero.api.net.web_utils import parse_url, argument_query, get_request
from golismero.api.plugin import TestingPlugin
from golismero.api.text.wordlist import WordListLoader
from golismero.api.text.text_utils import to_utf8
import time
from copy import copy

def payload_muntants(url_info, payload = {}, bmethod = 'GET', exclude_cgi_suffix = ['css', 'js', 'jpeg', 'jpg', 'png', 'gif', 'svg', 'txt'],
                     use_cache = None, timeout = 10.0 , bcheck_use_orig_body = True, req_header = {},
                     resp_code = '200', resp_header = {}, **kwargs):

    '''

    :param url_info:
    :param payload: {'k':'id', 'pos': 1, 'payload':str, 'type': 0}  (pos:0 key, pos:1 value) (type:0 append, type:1 replace)
    :param exclude_cgi_suffix:
    :param depth:
    :param bcheck_use_orig_body:
    :param req_header:
    :param resp_code:
    :param resp_header:
    :param kwargs:
    :return:
    '''
    if not isinstance(url_info , URL):
        raise TypeError("Expected url object, type:%s" % type(url_info))

    if not isinstance(payload, dict):
        raise TypeError("Excepted payload object, type:%s" % type(payload))

    if url_info.parsed_url.extension[1:] in exclude_cgi_suffix:
        Logger.log_verbose("Skipping URL: %s" % url_info.url)

    m_url_info = copy(url_info)
    if  bmethod == "GET":
        param_dict = copy(m_url_info.url_params)
    elif bmethod == "POST":
        param_dict = copy(m_url_info.post_params)

    if len(param_dict) == None and len(param_dict) == 0:
        return None

    __ = parse_url(m_url_info.url)

    k = payload['k']
    if payload['pos'] == 1:
        #value
        if payload['type'] == 0:  #append
            param_dict[k] = param_dict[k] + payload['payload']
        elif payload['type'] == 1:  #replace
            param_dict[k] = payload['payload']
    else:
        #key 先不考虑key值
        if payload['type'] == 0:
            param_dict.update(k = param_dict.pop(k))

        # TODO GET/POST param key need deal
        raise ValueError("GET/POST param key payload is not support!")

    retry_cnt = 0

    while retry_cnt < 3:
        if bmethod == "GET":
            m_resource_url_payload = URL(url = __.request_cgi, method = m_url_info.method, referer = m_url_info.referer, url_params= param_dict)

        elif bmethod == "POST":
            m_resource_url_payload = URL(url = __.request_cgi, method = m_url_info.method, referer = m_url_info.referer, post_params= param_dict)

        try:
            p = get_request(url = m_resource_url_payload, allow_redirects=False, use_cache = use_cache, timeout = timeout)
            return p

        except NetworkException, e:
            retry_cnt += 1
            time.sleep(0.5)
            Logger.log_error_verbose("Error while processing %r: %s" % (m_resource_url_payload.url, str(e)))

    return None