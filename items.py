# -*- coding: utf-8 -*-


import scrapy


class AqicrawlerItem(scrapy.Item):
    city_name = scrapy.Field()
    date = scrapy.Field()
    aqi = scrapy.Field()
    air_level = scrapy.Field()  # 空气质量等级
    pm25 = scrapy.Field()   # PM2.5
    pm10 = scrapy.Field()   # PM10
    so2 = scrapy.Field()    # SO2
    co = scrapy.Field()     # CO
    no2 = scrapy.Field()    # NO2
    o38h = scrapy.Field()   # O3_8h
