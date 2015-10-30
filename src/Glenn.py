#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# Date: 30/Oct/2015
# File: Glenn.py
# Desc: main class
#
# Produced By CSRGXTU
import urllib2

class Glenn(object):
    Url = None
    Method = None

    Code = None
    Msg = None
    Headers = None
    Body = None

    def __init__(self, url, method='GET'):
        self.Url = url
        self.Method = method

    def request(self):
        try:
            opener = urllib2.build_opener()
            handler = opener.open(self.Url)

            self.Code = handler.getcode()
            self.Msg = 'Success'
            self.Headers = handler.info()
            self.Body = heandler.read()

            handler.close()
        except urllib2.URLError, e:
            self.Code = 400
            self.Msg = 'Bad Request'
        except urllib2.HTTPError, e:
            self.Code = e.code
            self.Msg = e.reason
        finally:
            return self.Code

    def setHeader(self, dict):
        pass
