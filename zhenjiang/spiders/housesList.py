# -*- coding: utf-8 -*-
import scrapy
from zhenjiang.items import ZhenjiangItem


class HouseslistSpider(scrapy.Spider):
    name = 'housesList'
    allowed_domains = ['221.6.146.72:9080']
    # start_urls = ['http://221.6.146.72:9080/estate2/olestate/search2.action?cityId=&pre=%221%22']


    def start_requests(self):
        for i in range(1, 273):
            url = 'http://221.6.146.72:9080/estate2/olestate/search2.action?cityId=&pre=%221%22'
            form_data = {
                'pre': '%A3%A21%A3%A2',
                'currentPage': "{}".format(i),
            }
            yield scrapy.FormRequest(url, formdata=form_data, callback=self.parse_page)

    def parse_page(self, response):
        items = ZhenjiangItem()
        sTr = response.xpath('//tr[@class="tr_list"]')
        # print(response.status)
        if len(sTr) > 0:
            for sTd in sTr:
                # 城市
                sCityName = '镇江'
                # 楼盘详情链接
                sUrl = 'http://221.6.146.72:9080'
                sLink = sTd.xpath('./td[1]/a/@href').extract()[0]
                sHousingDetails = sUrl + sLink
                print(sHousingDetails)
                items['sHousingDetails'] = sHousingDetails
                # 楼盘
                sProjectName = sTd.xpath('./td[1]/a/font/text()').extract()[0].strip()
                items['sProjectName'] = sProjectName
                print(sProjectName)
                # 所含撞号
                sBuildName = sTd.xpath('./td[2]/text()').extract()[0]
                items['sBuildName'] = sBuildName
                print(sBuildName)
                # 地址
                sProjectAddress = sTd.xpath('./td[3]/text()').extract()[0]
                items['sProjectAddress'] = sProjectAddress
                print(sProjectAddress)
                # 管理区域
                sAreaName = sTd.xpath('./td[4]/text()').extract()[0]
                items['sProjectName'] = sProjectName
                print(sAreaName)
                # 可售套数
                sOnSaleNum = sTd.xpath('./td[5]/text()').extract()[0].strip()
                items['sOnSaleNum'] = sOnSaleNum
                print(sOnSaleNum)
                # 发布日期
                sPubDate = sTd.xpath('./td[6]/text()').extract()[0].strip()
                items['sPubDate'] = sPubDate
                print(sPubDate)
                yield items



