# -*- coding: utf-8 -*-

import base64

# proxyServer = "http://139.196.99.101:7036"
proxyServer = "http://183.129.207.82:12404"
#new
proxyUser = "H7U6815M699ESC0D"
proxyPass = "C3197EEF9AF366C2"
proxyAuth = "Basic " + str(base64.encodebytes(bytes(proxyUser + ":" + proxyPass, 'utf-8')), 'utf-8').strip()

class ProxyMiddleware(object):

    def process_request(self, request, spider):
        print("=============abuyun ==============", request.url)
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth
        #print 'request:', request.headers
        #print 'request:', request.meta
        #print 'request:', request.cookies