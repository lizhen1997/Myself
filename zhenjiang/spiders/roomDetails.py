# -*- coding: utf-8 -*-
import scrapy
import re


class RoomdetailsSpider(scrapy.Spider):
    name = 'roomDetails'
    allowed_domains = ['221.6.146.72:9080']
    start_urls = ['http://221.6.146.72:9080/']

    def parse(self, response):
        rel = re.compile(r"(建筑面积:\d+\.\d+)\s")
        rel2 = re.compile(r"(套内面积:.*\s.*\s.*\d)")
        rel3 = re.compile(r"(当前销售状态:)</font>(.*?)<br>")

        t1 = re.search(rel, response)
        print(t1.group(1))
        t2 = re.search(rel2, response)
        print(t2.group(1))
        t3 = re.findall(rel3, response)[0]
        print(t3[0], t3[1])

