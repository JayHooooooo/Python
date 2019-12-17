# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from txvideo.txvideo.items import Txurl


def getUrl(current):
    return 'https://v.qq.com/x/bu/pagesheet/list?_all=1&append=1&channel=movie&listpage=1&offset={0}&pagesize=30&sort=18'.format(
        str(current))


class TxvurlSpiderSpider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {
            'txvideo.pipelines.TxvideoPipeline': 300
        }
    }
    current = 0
    name = 'txvurl_spider'
    allowed_domains = ['v.qq.com']
    start_urls = ['http://v.qq.com/x/bu/pagesheet/list?_all=1&append=1&channel=movie&listpage=1&offset0&pagesize=30&sort=18']

    def parse(self, response):
        # 响应正确
        if response.status == 200:
            item = Txurl()
            divs = response.xpath("//div[@class='figure_detail figure_detail_two_row']")
            links = [div.xpath(".//a/@href").get() for div in divs]
            names = [div.xpath(".//a/text()").get() for div in divs]
            item['urls'] = tuple(zip(links, names))
            TxvurlSpiderSpider.current += 30
            yield item
            yield scrapy.Request(getUrl(TxvurlSpiderSpider.current), self.parse)
        else:
            return

