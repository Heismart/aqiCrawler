# -*- coding: utf-8 -*-

import re
import scrapy
from urlparse import urljoin
from ..items import AqicrawlerItem
from urllib import unquote


class AqiSpider(scrapy.Spider):
    name = 'aqi'
    allowed_domains = ['aqistudy.cn']
    start_urls = ['https://www.aqistudy.cn/historydata/']
    BASE_URL = "https://www.aqistudy.cn/historydata/"

    def parse(self, response):
        city_urls = response.xpath("//ul[@class='unstyled']//li/a/@href").extract()
        for item in city_urls:
            url = urljoin(self.BASE_URL, item)
            yield scrapy.Request(url, callback=self.parse_month)

    def parse_month(self, response):
        month_urls = response.xpath("//ul[@class='unstyled1']/li/a/@href").extract()
        for item in month_urls:
            url = urljoin(self.BASE_URL, item)
            yield scrapy.Request(url, callback=self.parse_day)

    def parse_day(self, response):
        nodes = response.xpath("//tbody/tr")[1:]
        for node in nodes:
            item = AqicrawlerItem()
            name = re.search(r'city=(.*?)&', response.url)
            item["city_name"] = unquote(name.group(1)) if name else ''
            item["date"] = node.xpath("./td[1]/text()").extract_first()
            item["aqi"] = node.xpath("./td[2]/text()").extract_first()
            item["air_level"] = node.xpath("./td[3]/span/text()").extract_first()
            item["pm25"] = node.xpath("./td[4]/text()").extract_first()
            item["pm10"] = node.xpath("./td[5]/text()").extract_first()
            item["so2"] = node.xpath("./td[6]/text()").extract_first()
            item["co"] = node.xpath("./td[7]/text()").extract_first()
            item["no2"] = node.xpath("./td[8]/text()").extract_first()
            item["o38h"] = node.xpath("./td[9]/text()").extract_first()
            # print(item)
            yield item
