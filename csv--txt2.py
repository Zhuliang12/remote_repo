# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/11/27 19:18

import pandas as pd
import os

# 读取news_data.csv，保存到新建的news_data.txt中
data = pd.read_csv('train.csv', encoding='utf-8')
with open('train.txt', 'a+', encoding='utf-8') as f:
    for line in data.values:
        # str(line[0])：csv中第0列；+','+：csv两列之间保存到txt用逗号（，）隔开；'\n'：读取csv每行后在txt中换行
        f.write((str(line[0]) + ',' + str(line[3]) + ',' + str(line[4]) + '\n'))

