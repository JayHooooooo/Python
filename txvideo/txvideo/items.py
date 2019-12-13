# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Txurl(scrapy.Item):
    urls = scrapy.Field()


class Txvideo(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    detail = scrapy.Field()
    casts = scrapy.Field()
    director = scrapy.Field()
    tags = scrapy.Field()
    amount = scrapy.Field()