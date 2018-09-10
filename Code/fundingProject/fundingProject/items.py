# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FundingprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    project_name = scrapy.Field()
    authorization_number = scrapy.Field()
    category = scrapy.Field()
    school = scrapy.Field()
    leader = scrapy.Field()
    expenditure = scrapy.Field()
    approval_year = scrapy.Field()
    key_word = scrapy.Field()