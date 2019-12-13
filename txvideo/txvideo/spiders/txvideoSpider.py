# -*- coding: utf-8 -*-
import scrapy

from txvideo.LinesUtils import Lines
from txvideo.items import Txvideo


class TxvideospiderSpider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {
            'txvideo.pipelines.TxvideosPipeline': 301
        }
    }

    name = 'txvideoSpider'
    allowed_domains = ['v.qq.com']
    start_urls = [Lines.getUrl()]

    def parse(self, response):
        item = Txvideo()
        try:
            item['title'] = response.xpath("//h1[@class='video_title _video_title']/text()").get().strip()
            score_int = response.xpath("//span[@class='video_score']/span[@class='units']/text()").get().strip()
            score_deci = response.xpath("//span[@class='video_score']/span[@class='decimal']/text()").get().strip()
            item['score'] = score_int + score_deci
            item['detail'] = response.xpath("//p[@class='summary']/text()").get()
            casts = response.xpath("//a[@class='name']/text()").getall()
            item['casts'] = ','.join([cast.strip() for cast in casts])
            item['director'] = response.xpath("//div[@class='director']")[0].xpath('.//a/text()').get()
            tags = response.xpath("//div[@class='video_tags _video_tags']/a/text()").getall()
            item['tags'] = ','.join(tags)
            item['amount'] = response.xpath("//em[@id='mod_cover_playnum']/text()").get()
        except Exception as e:
            print(e)
        # 处理此item
        yield item
        # 告知队列管理器调度下一个
        scrapy.Request.headers = {
            'referer': 'https://v.qq.com/'
        }
        yield scrapy.Request(Lines.getUrl(), self.parse)
