# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhenjiangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sHousingDetails = scrapy.Field()
    sProjectName = scrapy.Field()
    sBuildName = scrapy.Field()
    sProjectAddress = scrapy.Field()
    sAreaName = scrapy.Field()
    sOnSaleNum = scrapy.Field()
    sPubDate = scrapy.Field()


class HousesParticularsItem(scrapy.Item):
    SHousingDetails = scrapy.Field()
    sProjectNameAlias = scrapy.Field()
    sProjectName = scrapy.Field()
    sBuildName = scrapy.Field()
    sPresellCode = scrapy.Field()
    sDeveloper = scrapy.Field()
    sProjectAddress = scrapy.Field()
    sAreaName = scrapy.Field()
    sProjectUse = scrapy.Field()
    sConstructStartDate = scrapy.Field()
    sConstructEndDate = scrapy.Field()