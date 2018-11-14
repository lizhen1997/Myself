# -*- coding: utf-8 -*-
import scrapy


class HousesdetailsSpider(scrapy.Spider):
    name = 'housesDetails'
    allowed_domains = ['221.6.146.72:9080']
    start_urls = ['http://221.6.146.72:9080/']

    def parse(self, response):
        div = response.xpath('/html/body/div/table[2]/tr[1]/td[2]/div/table[2]/tr[1]/td/table/tbody/tr')[1:-1]
        for d in div:
            sUrl = 'http://221.6.146.72:9080'
            l = response.xpath('./td[1]/a/@herf').extract()[0]
            link = sUrl + l
            print(link)
            d1 = d.xpath("./td[1]//font/text()").extract()[0]
            print(d1)
            t2 = d.xpath("./td[2]/text()")
            t2 = "/".join(t2)
            print(t2)
            t3 = d.xpath("./td[3]/text()").extract()[0]
            print(t3)
            t4 = d.xpath("./td[4]/text()").extract()[0]
            print(t4)
            t5 = d.xpath("./td[5]/text()").extract()[0]
            print(t5)
            t6 = d.xpath("./td[6]/text()").extract()[0]
            print(t6)
            t7 = d.xpath("./td[3]/text()").extract()[0]
            print(t7)
            t8 = d.xpath("./td[8]/text()").extract()[0]
            print(t8)