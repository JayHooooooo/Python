import sys

current_working_directory = r"C:\Users\Hoo\Documents\workspace\python\tencent"
sys.path.append(current_working_directory)

import numpy as np
import pandas as pd

from matplotlib import font_manager as fm
from matplotlib import cm
from matplotlib import pyplot as plt
from txvideo.txvideo.analysis.db_getDate import Data

if __name__ == '__main__':
    data = Data()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    shapes = list(sys.argv[1:])
    values = data.categoryDate(shapes)
    s = pd.Series(values, index=shapes)
    labels = s.index
    sizes = s.values
    # explode = (0.1, 0, 0)  # "explode" ， show the selected slice
    explode = tuple(float(item / 1000) for item in values)
    fig, axes = plt.subplots(figsize=(8, 5), ncols=2)  # 设置绘图区域大小
    ax1, ax2 = axes.ravel()

    colors = cm.rainbow(np.arange(len(sizes)) / len(sizes))  # colormaps: Paired, autumn, rainbow, gray,spring,Darks
    patches, texts, autotexts = ax1.pie(sizes, labels=labels, autopct='%1.0f%%', explode=explode,
                                        shadow=False, startangle=170, colors=colors, labeldistance=1.2,
                                        pctdistance=1.1, radius=0.4)
    # labeldistance: 控制labels显示的位置
    # pctdistance: 控制百分比显示的位置
    # radius: 控制切片突出的距离

    ax1.axis('equal')

    # 重新设置字体大小
    proptease = fm.FontProperties()
    proptease.set_size('medium')
    # font size include: ‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xx-large’ or number, e.g. '12'
    plt.setp(autotexts, fontproperties=proptease)
    plt.setp(texts, fontproperties=proptease)

    ax1.set_title('腾讯视频电影分类统计', loc='center')

    # ax2 只显示图例（legend）
    ax2.axis('off')
    ax2.legend(patches, labels, loc='center left')

    plt.tight_layout()
    # plt.savefig("pie_shape_ufo.png", bbox_inches='tight')
    plt.savefig('Demo_project_final.png')
    plt.show()
