# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2023/3/30 15:42

import matplotlib.pyplot as plt
import numpy as np

# epoch,acc,loss,val_acc,val_loss


# 画图
# plt.plot(x_axis_data, y_axis_data1, 'b*--', alpha=0.5, linewidth=1, label='acc')  # '
# plt.plot(x_axis_data, y_axis_data2, 'rs--', alpha=0.5, linewidth=1, label='acc')
# plt.plot(x_axis_data, y_axis_data3, 'go--', alpha=0.5, linewidth=1, label='acc')



# plt.ylim(-1,1)#仅设置y轴坐标范围
# plt.show()
train_cls = []
valid_cls = []
epoch = []
with open('results.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        # print(line)
        # line.strip()
        a = float(line[101:111])
        b = int(line[1:6]) + 1
        train_cls.append(a)
        epoch.append(b)

with open('wiou.txt', 'r') as f1:
    lines = f1.readlines()
    for line in lines:
        a = float(line[101:111])
        valid_cls.append(a)

print(valid_cls)


print(train_cls)
print(epoch)
print(type(valid_cls))

plt.plot(epoch[:200],train_cls[0:200] , 'b-', alpha=1, linewidth=1, label='ori_valid_mAP')
plt.plot(epoch[:200], valid_cls[:200], 'r-', alpha=1, linewidth=1, label='update_valid_mAP')
plt.legend()
plt.xlabel('epoch')
plt.ylabel('mAP')
plt.show()
