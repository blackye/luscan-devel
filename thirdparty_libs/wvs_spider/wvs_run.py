#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys

from thirdparty_libs.wvs_spider.wvs_console import WVSSpider


def do_wvs_crawl(target, keys):
	print 'start crawl %s, keys:%s' % (target, keys)
	WVSSpider(target, keys).start()


#def run_wvs_spider(target):
#	result = do_wvs_crawl(target)


def main():
	if len(sys.argv) == 3:
		print 'fuck!!!!'
		do_wvs_crawl(sys.argv[1], sys.argv[2])


if __name__  == '__main__': main()