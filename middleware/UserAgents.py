#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:   Travis A. Ebesu
@created:  2014-08-19
@summary:  Scrapy middleware that rotates user agents
'''
# Randomly select
from random import choice
# Gets the current path
from os.path import abspath, dirname
from inspect import currentframe, getfile
# pylint: disable=C0301

class UserAgentsMiddleware(object):
    '''
    Scrapy User Agent Rotator Middleware
    See the original middleware to understand this code better:
        https://github.com/scrapy/scrapy/blob/master/scrapy/contrib/downloadermiddleware/useragent.py

    Specify the filename in the settings file
    '''
    def __init__(self, filename):
        '''
        Load our useragents list file and parse it
        '''
        #path = getcwd() + '/' + filename
        # Gets this files current path
        path = dirname(abspath(getfile(currentframe()))) + '/' + filename
        with open(path) as f:
            self.useragent_list = [line.strip() for line in f.readlines()]

    @classmethod
    def from_crawler(cls, crawler):
        '''
        Get our user agent list filename, this gets passed to our class init
        '''
        return cls(crawler.settings.get('USER_AGENT_LIST'))


    def process_request(self, request, spider):
        '''
        Each request is sent through middleware. We randomly select a user agent
        and set it as the default for each time
        '''
        request.headers.setdefault('User-Agent', choice(self.useragent_list))


if __name__ == '__main__':
    pass
