# -*- coding: utf-8 -*-
import scrapy
from ..items import PatentsItem
import re


class PatentSpider(scrapy.Spider):
    name = 'patent'
    # allowed_domains = ['npd.nsfc.gov.cn']
    # start_urls = ['http://npd.nsfc.gov.cn/']
    start_urls = []
    for currentPage in range(1, 5613):
        new_start_urls = 'http://npd.nsfc.gov.cn/OutComeSearch.action?outcomeCategory=patent&currentPage=' \
                         + str(currentPage)
        start_urls.append(new_start_urls)

    def parse(self, response):
        item = PatentsItem()
        for info in response.xpath("//dl[@class='time_dl']"):
            patent_name = info.xpath("dt//text()").extract()
            item['patent_name'] = re.sub(r'\s+', '', ''.join(patent_name))  # 正则表达式，去除空格
            inventors = info.xpath("dd[1]/text()").extract()
            item['inventors'] = re.sub(r'\s+', '', ''.join(inventors).replace('发明hahah人：', ''))
            license_unit = info.xpath("dd[2]/text()").extract()
            item['license_unit'] = re.sub(r'\s+', '', ''.join(license_unit).replace('发证单位：', ''))
            support_unit = info.xpath("dd[3]/text()").extract()
            item['support_unit'] = re.sub(r'\s+', '', ''.join(support_unit)).replace('依托单位：', '')
            date = info.xpath("dd[4]/text()").extract()
            item['date'] = re.sub(r'\s+', '', ''.join(date).replace('授奖日期：', ''))
            patent_type = info.xpath("dd[5]/text()").extract()
            item['patent_type'] = re.sub(r'\s+', '', ''.join(patent_type).replace('专利类型：', ''))
            project_name = info.xpath("dd[6]//text()").extract()
            item['project_name'] = re.sub(r'\s+', '', ''.join(project_name).replace('相关项目：', ''))
            yield item

