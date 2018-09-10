# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import FinishedprojectItem


class FipSpider(scrapy.Spider):
    name = 'fip'
    # allowed_domains = ['npd.nsfc.gov.cn']
    # start_urls = ['http://npd.nsfc.gov.cn/']
    start_urls = []
    for currentPage in range(1, 20140):
        new_start_urls = 'http://npd.nsfc.gov.cn/projectSearch!search.action??currentPage=' \
                         + str(currentPage)
        start_urls.append(new_start_urls)

    def parse(self, response):
        item = FinishedprojectItem()
        for info in response.xpath("//dl[@class='time_dl']"):
            project_name = info.xpath("dt//text()").extract()
            item['project_name'] = re.sub(r'\s+', '', ''.join(project_name))  # 正则表达式，去除空格
            authorization_number = info.xpath("dd[1]/text()").extract()
            item['authorization_number'] = re.sub(r'\s+', '', ''.join(authorization_number).replace('批准号：', ''))
            category = info.xpath("dd[2]/text()").extract()
            item['category'] = re.sub(r'\s+', '', ''.join(category).replace('项目类别：', ''))
            school = info.xpath("dd[3]//text()").extract()
            item['school'] = re.sub(r'\s+', '', ''.join(school)).replace('依托单位：', '')
            leader = info.xpath("dd[4]//text()").extract()
            item['leader'] = re.sub(r'\s+', '', ''.join(leader).replace('项目负责人：', ''))
            expenditure = info.xpath("dd[5]/text()").extract()
            item['expenditure'] = float(
                re.sub(r'\s+', '', ''.join(expenditure).replace('资助经费：', '')).replace('（万元）', ''))
            research_achievements = info.xpath("dd[6]//text()").extract()
            item['research_achievements'] = re.sub(r'\s+', '', ''.join(research_achievements).replace('研究成果：', ''))
            yield item

