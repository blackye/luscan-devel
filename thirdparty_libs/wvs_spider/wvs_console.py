#!/usr/bin/env/python
#-*- coding:utf-8 -*-

__author__ = 'BlackYe.'

import os, datetime, time, urllib, random, hashlib, threading, subprocess
from lib.config import XML_SAVE_PATH
from lib.config import WVS_INSTALL_PATH

class WVSSpider(threading.Thread):

    def __init__(self, url, keys):
        super(WVSSpider, self).__init__()
        self.url = url
        self.save_folder_name = keys
        

    def _get_wvs_console_path(self):
        return WVS_INSTALL_PATH

    def get_run_cmd(self):
    	save_folder_path = XML_SAVE_PATH + self.save_folder_name
        print save_folder_path
    	return '{0}/wvs_console.exe /Crawl {1}  /ExportXML /SaveLogs /Settings Default /SaveCrawlerData /SaveFolder {2} --EnablePortScanning=False --ManipHTTPHeaders=True'.format(self._get_wvs_console_path(), self.url, save_folder_path) 

    def run(self):
    	self.__spider_proc = subprocess.Popen(args=self.get_run_cmd(),
                                               stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE,
                                                bufsize=0)
        print self.__spider_proc.stdout.readlines()
		


def main():
	wvs_spider = WVSSpider(url = 'http://www.baidu.com/afdasf')
	wvs_spider.start()
    


if __name__  == '__main__': main()
