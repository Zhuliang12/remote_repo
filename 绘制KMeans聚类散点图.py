# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/3/26 16:15

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# 生成随机数据
X = np.random.rand(1000, 2)
# 创建KMeans模型并拟合数据
kmeans = KMeans(n_clusters=10, random_state=0).fit(X)
labels = kmeans.labels_
# 绘制散点图
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.show()