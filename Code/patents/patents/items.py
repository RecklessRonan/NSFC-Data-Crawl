# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PatentsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    patent_name = scrapy.Field()
    inventors = scrapy.Field()
    license_unit = scrapy.Field()
    support_unit = scrapy.Field()
    date = scrapy.Field()
    patent_type = scrapy.Field()
    project_name = scrapy.Field()


