#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/10/13 15:29

import os

cnt = 0

txt_path = r'C:\Users\liang\Desktop\all\test\labels/'

txt_files = os.listdir(txt_path)

for file in txt_files:
    path = os.path.join(txt_path, file)
    with open(path, 'rb') as f:
        for line in f:
            cnt += 1

print(cnt)
