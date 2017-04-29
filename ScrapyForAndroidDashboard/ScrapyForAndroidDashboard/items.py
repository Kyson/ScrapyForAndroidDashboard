# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyforandroiddashboardItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    version_data = scrapy.Field()
    version_names = scrapy.Field()
    screen_data = scrapy.Field()


class AndroidVersionItem(scrapy.Item):
    version_code = scrapy.Field()
    version_name = scrapy.Field()
    version_api = scrapy.Field()
    version_distribution = scrapy.Field()


class AndroidVersionChartItem(scrapy.Item):
    chart_url = scrapy.Field()
