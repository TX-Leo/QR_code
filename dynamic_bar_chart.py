# made by wangzhi
# TX_Leo
'''生成一个动图gif：日期变化与在一起等标志'''
'''
8.14
距4.27   110天
距5.20   86天
'''
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import pandas as pd
import datetime

df = pd.read_excel("数据1.xlsx")
df['日期文本'] = df['日期'].apply(lambda x: str(x)[:10])
t = datetime.datetime(2021,4,27) # 起始日期
fig, ax = plt.subplots(figsize=(10,6)) # 画布
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 字体设为微软雅黑
timeSlot = [x for x in range(0,110)] # 时间轴（一共最大110天）
colors = ['#ADD8E6', '#DC143C', '#FFC0CB'] # 颜色列表

def draw(date):
    print(date)
    # 数据处理 ------
    current_date = (t + datetime.timedelta(days=date)).strftime("%Y-%m-%d")
    df_ = df[df['日期文本'].eq(current_date)]
    days = df_['天数']
    item = df_["项目"]
    # 绘制条形图 ------
    ax.clear() # 重绘
    ax.barh(item, days, color = colors)
    for y, (x,name) in enumerate(zip(days.values,item.values)): # 系列标注
            ax.text(x, y, "%s" % x, size=12)
            if x > 1:
                ax.text(x-0.5, y, name, size=14, ha = 'right')
    ax.text(1, 1.01, current_date, transform = ax.transAxes, size= 20, ha='right') # 滚动时间
    ax.get_xaxis().set_visible(False) # 隐藏坐标轴
    ax.get_yaxis().set_visible(False)

# draw(19)
# plt.savefig('test.png')
animator = ani.FuncAnimation(fig, draw, frames=timeSlot ,interval = 100) # interval时间间隔
plt.show()
animator.save('process.gif',fps=5)#生成动图gif