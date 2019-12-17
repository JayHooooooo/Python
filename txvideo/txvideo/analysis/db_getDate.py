import sys

import pymysql

current_working_directory = r"C:\Users\Hoo\Documents\workspace\python\tencent"
sys.path.append(current_working_directory)


class Data(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='www.jayhoo.top',
            user='python',
            password='Python123_',
            database='spider',
            port=3306,
            charset='utf8'
        )

    def tagPercentage(self, name):
        select_sql = "SELECT SUM(`tags` LIKE %s) / COUNT(*) AS rs FROM `txc_videos`"
        cursor = self.conn.cursor()
        try:
            cursor.execute(select_sql, ''.join(['%', str(name), '%']))
            rs = cursor.fetchone()
            return rs[0]
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def categoryDate(self, name):
        data = Data()
        rs = [data.tagPercentage(item) * 100 for item in name]
        return rs

    def scoreStuation(self):
        select_sql = r"SELECT " \
                     r"SUM(`score` >= 9 AND `score` <= 10 ) AS '[9-10]'," \
                     r"SUM(`score` >= 8 AND `score` < 9) AS '[8-9)'," \
                     r"SUM(`score` >= 7 AND `score` < 8) AS '[7-8)'," \
                     r"SUM(`score` >= 6 AND `score` < 7) AS '[6-7)'," \
                     r"SUM(`score` < 6) AS '[0-6)'" \
                     r"FROM `txc_videos`"
        cursor = self.conn.cursor()
        try:
            cursor.execute(select_sql)
            rs = cursor.fetchall()
            des = cursor.description
            return {
                'des': tuple(item[0] for item in des),
                'ranking':  [float(item) for item in rs[0]]
            }
        except Exception as e:
            print(e)
        finally:
            cursor.close()

