# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/2/18 20:18

import pandas as pd
from collections import defaultdict

train_df=pd.read_csv('D:/mydata/stervel/severstal-steel-defect-detection/train.csv')
sample_df=pd.read_csv('D:/mydata/stervel/severstal-steel-defect-detection/sample_submission.csv')

print(train_df.head())
print('\r\n')
print(sample_df.head())

class_dict = defaultdict(int)
kind_class_dict = defaultdict(int)
no_defects_num = 0
defects_num = 0

# 接下来统计有无缺陷及每类缺陷的图像数量
for col in range(0, len(train_df), 4):
    img_names = [str(i).split("_")[0] for i in train_df.iloc[col:col+4, 0].values]
    if not (img_names[0] == img_names[1] == img_names[2] == img_names[3]):
        raise ValueError

    labels = train_df.iloc[col:col+4, 1]
    if labels.isna().all():
        no_defects_num += 1
    else:
        defects_num += 1

    kind_class_dict[sum(labels.isna().values == False)] += 1

    for idx, label in enumerate(labels.isna().values.tolist()):
        if label == False:
            class_dict[idx+1] += 1

print("无缺陷钢板数量: {}".format(no_defects_num))
print("有缺陷钢板数量: {}".format(defects_num))
'''
无缺陷钢板数量: 5902
有缺陷钢板数量: 6666
'''

# 对有缺陷的图像进行分类统计
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
sns.barplot(x=list(class_dict.keys()), y=list(class_dict.values()), ax=ax)
ax.set_title("the number of images for each class")
ax.set_xlabel("class")
plt.show()
print(class_dict)

# 统计一张图像中可能包含的缺陷种类数
fig, ax = plt.subplots()
sns.barplot(x=list(kind_class_dict.keys()), y=list(kind_class_dict.values()), ax=ax)
ax.set_title("Number of classes included in each image");
ax.set_xlabel("number of classes in the image")
plt.show()
print(kind_class_dict)



