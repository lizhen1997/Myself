# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re


class XinfangSpider(scrapy.Spider):
    name = 'xinfang'
    allowed_domains = ['221.6.146.72']
    start_urls = ['http://221.6.146.72:9080/estate2/olestate/search2.action?cityId=&pre=%221%22']

    def parse(self, response):
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
                # # 楼盘
                # sProjectName = sTd.xpath('./td[1]/a/font/text()').extract()[0].strip()
                # print(sProjectName)
                # # 所含撞号
                # sBuildName = sTd.xpath('./td[2]/text()').extract()[0]
                # print(sBuildName)
                # # 地址
                # sProjectAddress = sTd.xpath('./td[3]/text()').extract()[0]
                # print(sProjectAddress)
                # # 管理区域
                # sAreaName = sTd.xpath('./td[4]/text()').extract()[0]
                # print(sAreaName)
                # # 可售套数
                # sOnSaleNum = sTd.xpath('./td[5]/text()').extract()[0].strip()
                # print(sOnSaleNum)
                # # 发布日期
                # sPubDate = sTd.xpath('./td[6]/text()').extract()[0].strip()
                # print(sPubDate)
                if len(sHousingDetails) > 0:
                    yield scrapy.Request(sHousingDetails, callback=self.parse_housing_details)

    def parse_housing_details(self, response):
        listA = []
        soup = BeautifulSoup(response.text, "lxml")
        lhref = soup.find_all(name="table")[1].find_all(name="td")[1].find_all("tr")[0].find_all("a")[1].attrs['href']
        sUrl = 'http://221.6.146.72:9080'
        SHousingDetails = sUrl + lhref
        print(SHousingDetails)

        # sTrs = soup.find_all(name="table")[1].find_all(name="table")[3].find_all("td")[2:]
        # for sTd in sTrs:
        #     listA.append(sTd.string)
        # # 楼盘暂定名
        # pat1 = re.search(r'&nbsp;(.*?)\s+\(点击此处浏览', response.text)
        # sProjectNameAlias = pat1.group(1).strip()
        # print(sProjectNameAlias)
        # # 楼盘现定名
        # sProjectName = listA[4].strip()
        # print(sProjectName)
        # # 包含幢号
        # sBuildName = listA[6].strip()
        # print(sBuildName)
        # # 预(销)售许可证号
        # sPresellCode = listA[8].strip()
        # print(sPresellCode)
        # # 开发商
        # sDeveloper = response.xpath('//tr/td[contains(text(), "开发商")]/following-sibling::td/a').extract()[0].strip()
        # print(sDeveloper)
        # # 坐落
        # sProjectAddress = listA[16].strip()
        # print(sProjectAddress)
        # # 规划用途
        # sProjectUse = listA[18].strip()
        # print(sProjectUse)
        # # 开工日期
        # sConstructStartDate = listA[34].strip()
        # print(sConstructStartDate)
        # # 预计竣工日期
        # sConstructEndDate = listA[36].strip()
        # print(sConstructEndDate)
        if len(SHousingDetails) > 0:
            yield scrapy.Request(SHousingDetails, callback=self.parse_housing_details_list)

    def parse_housing_details_list(self, response):
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
            if len(link) > 0:
                yield scrapy.Request(link, callback=self.AAA)
    def AAA(self,response):
        rel = re.compile(r"(建筑面积:\d+\.\d+)\s")
        rel2 = re.compile(r"(套内面积:.*\s.*\s.*\d)")
        rel3 = re.compile(r"(当前销售状态:)</font>(.*?)<br>")

        t1 = re.search(rel, response)
        print(t1.group(1))
        t2 = re.search(rel2, response)
        print(t2.group(1))
        t3 = re.findall(rel3, response)[0]
        print(t3[0], t3[1])

