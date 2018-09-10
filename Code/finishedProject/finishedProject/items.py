# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FinishedprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    project_name = scrapy.Field()
    authorization_number = scrapy.Field()
    category = scrapy.Field()
    school = scrapy.Field()
    leader = scrapy.Field()
    expenditure = scrapy.Field()
    research_achievements = scrapy.Field()
