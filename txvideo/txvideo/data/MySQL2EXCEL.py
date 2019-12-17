import sys
import pymysql
import xlwt
import time

def getDB():
    try:
        conn = pymysql.connect(
            host='www.jayhoo.top',
            user='python',
            password='Python123_',
            database='spider',
            port=3306,
            charset='utf8'
        )
        return conn
    except Exception as e:
        print(e)


def toExcel(conn, sql, path, file):
    # 边框的定义
    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    borders.bottom_colour = 0x3A
    # Initialize a style for frist row
    style_fristRow = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'Times New Roman'
    font.bold = True
    font.colour_index = 1
    style_fristRow.font = font

    badBG = xlwt.Pattern()
    badBG.pattern = badBG.SOLID_PATTERN
    badBG.pattern_fore_colour = 6
    style_fristRow.pattern = badBG

    style_fristRow.borders = borders

    # Initialize a style for data row
    style_dataRow = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = u'隶变-简 常规体'
    font.bold = False
    style_dataRow.font = font

    style_dataRow.borders = borders

    cursor = conn.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    fields = cursor.description
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('mag', cell_overwrite_ok=True)
    #写字段信息
    for field in range(0, len(fields)):
        sheet.write(0, field, fields[field][0], style_fristRow)
    # 获取并写入数据段信息
    row = 1
    col = 0
    for row in range(1, len(datas) + 1):
        for col in range(0, len(fields)):
            sheet.write(row, col, u'%s' % datas[row - 1][col], style_dataRow)

    workbook.save(r'{exportPath}/{exportName}.xls'.format(exportPath=path, exportName=file))
    cursor.close()
    conn.close()

sql = "SELECT `id`,`title`,`score`,`datail`,`director`,`cast`,`tags`,`tags` FROM `txc_videos` "
now = time.time()
toExcel(getDB(), sql, './', 'movie')
print('use {second}s'.format(second=(time.time() - now)))

