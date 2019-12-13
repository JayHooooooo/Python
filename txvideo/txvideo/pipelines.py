# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class TxvideoPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='www.jayhoo.top',
            user='python',
            password='Python123_',
            database='spider',
            port=3306,
            charset='utf8'
        )

    def process_item(self, item, spider):
        insert_sql = 'INSERT INTO txv_video_url (url,name) VALUES (%s,%s)'
        try:
            cursor = self.conn.cursor()
            cursor.executemany(insert_sql, item['urls'])
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item


class TxvideosPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(
            host='www.jayhoo.top',
            user='python',
            password='Python123_',
            database='spider',
            port=3306,
            charset='utf8'
        )

    def process_item(self, item, spider):
        insert_sql = 'INSERT INTO `txc_videos` (`title`,`score`,`datail`,`cast`,`director`,`tags`,`amount`) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        try:
            cursor = self.conn.cursor()
            cursor.execute(insert_sql, (item['title'], item['score'], item['detail'], item['casts'], item['director'], item['tags'], item['amount']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
