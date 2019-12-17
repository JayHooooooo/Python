import matplotlib.pyplot as plt

from txvideo.txvideo.analysis.db_getDate import Data

data = Data()

rs = data.scoreStuation()
des = rs['des']
ranking = rs['ranking']

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel('评分情况')
plt.ylabel('对应评分电影数')
plt.title('腾讯视频电影评分表')
plt.bar(des, ranking, color='#ababab')
for i in range(len(ranking)):
    plt.text(des[i], ranking[i], '%d' % ranking[i], ha='center', va='bottom', fontsize=11)
plt.show()
