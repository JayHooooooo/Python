"""
介绍
  爬虫队列，从数据库读出相应条数链接，到条数剩余量不足时向数据请求的新的地址
原因
  减少内存中地址的数量，降低计算机硬件压力，平衡爬虫速度
"""
import time

import pymysql
import _thread
from scrapy import cmdline


class Lines(object):
    current = 0
    step = 1000
    urls = []
    conn = None

    @classmethod
    def getNext(clz):
        if not clz.conn:
            clz.conn = pymysql.connect(
                host='www.jayhoo.top',
                user='python',
                password='Python123_',
                database='spider',
                port=3306,
                charset='utf8'
            )
        select_sql = 'SELECT `url` FROM `txv_video_url` WHERE id BETWEEN %s AND %s'
        sql_max = 'SELECT MAX(id) FROM `txc_videos`'
        cursor = clz.conn.cursor()
        cursor.execute(sql_max)
        clz.current = cursor.fetchone()[0]
        cursor.execute(select_sql, (clz.current, clz.current + clz.step))
        url = cursor.fetchall()
        if not url:
            print('--------------\n spider is gone\n')
            exit(0)
        clz.urls += [url_[0] for url_ in url]

    @classmethod
    def getUrl(clz):
        if not clz.urls:
            clz.getNext()
        return clz.urls.pop()


if __name__ == '__main__':
    cmdline.execute(['scrapy', 'crawl', 'txvideoSpider'])
