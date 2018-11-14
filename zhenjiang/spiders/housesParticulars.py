# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re
from zhenjiang.item

class HousesparticularsSpider(scrapy.Spider):
    name = 'housesParticulars'
    allowed_domains = ['221.6.146.72:9080']
    start_urls = ['http://221.6.146.72:9080/']

    def parse(self, response):
        listA = []
        soup = BeautifulSoup(response.text, "lxml")
        lhref = soup.find_all(name="table")[1].find_all(name="td")[1].find_all("tr")[0].find_all("a")[1].attrs['href']
        sUrl = 'http://221.6.146.72:9080'
        SHousingDetails = sUrl + lhref
        print(SHousingDetails)

        sTrs = soup.find_all(name="table")[1].find_all(name="table")[3].find_all("td")[2:]
        for sTd in sTrs:
            listA.append(sTd.string)
        # 楼盘暂定名
        pat1 = re.search(r'&nbsp;(.*?)\s+\(点击此处浏览', response.text)
        sProjectNameAlias = pat1.group(1).strip()
        print(sProjectNameAlias)
        # 楼盘现定名
        sProjectName = listA[4].strip()
        print(sProjectName)
        # 包含幢号
        sBuildName = listA[6].strip()
        print(sBuildName)
        # 预(销)售许可证号
        sPresellCode = listA[8].strip()
        print(sPresellCode)
        # 开发商
        sDeveloper = response.xpath('//tr/td[contains(text(), "开发商")]/following-sibling::td/a').extract()[0].strip()
        print(sDeveloper)
        # 坐落
        sProjectAddress = listA[16].strip()
        print(sProjectAddress)
        # 规划用途
        sProjectUse = listA[18].strip()
        print(sProjectUse)
        # 开工日期
        sConstructStartDate = listA[34].strip()
        print(sConstructStartDate)
        # 预计竣工日期
        sConstructEndDate = listA[36].strip()
        print(sConstructEndDate)