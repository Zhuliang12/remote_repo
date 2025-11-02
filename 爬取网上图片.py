#  Institution: Leapting Technology
#  Author：liang zhu
#  Time：2023/10/23 13:00

import time
import requests
import urllib
from bs4 import BeautifulSoup
import requests

url = 'https://cn.bing.com/images/search'
params = {
    'q': '猫咪',
    'form': 'HDRSC2',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
}

response = requests.get(url, params=params, headers=headers)
print('response:', f'{response}')

if response.status_code == 200:
    html_content = response.text
else:
    print(f'Request failed with status code: {response.status_code}')
    html_content = None

soup = BeautifulSoup(html_content, 'html.parser')
image_elements = soup.find_all('img')

image_urls = []
for img in image_elements:
    if 'src' in img.attrs:
        image_urls.append(img['src'])

for index, url in enumerate(image_urls):
    response = requests.get(url)

    if response.status_code == 200:
        with open(f'C:/Users/liang/Desktop/solar_panel/image{index}.jpg', 'wb') as f:
            f.write(response.content)
    else:
        print(f'Download failed for image{index}.jpg')

# page = input("请输入要爬取多少页：")
# page = int(page) + 1  # 确保其至少是一页，因为 输入值可以是 0
# header = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
# }
# n = 0  # 图片的前缀 如 0.png
# pn = 1  # pn是从第几张图片获取 百度图片下滑时默认一次性显示30张
# for m in range(1, page):
#     url = 'https://image.baidu.com/search/acjson?'
#     param = {
#         'tn': 'resultjson_com',
#         'logid': '8846269338939606587',
#         'ipn': 'rj',
#         'ct': '201326592',
#         'is': '',
#         'fp': 'result',
#         'queryWord': '光伏组件脱落',
#         'cl': '2',
#         'lm': '-1',
#         'ie': 'utf-8',
#         'oe': 'utf-8',
#         'adpicid': '',
#         'st': '-1',
#         'z': '',
#         'ic': '',
#         'hd': '',
#         'latest': '',
#         'copyright': '',
#         'word': '光伏组件脱落',
#         's': '',
#         'se': '',
#         'tab': '',
#         'width': '',
#         'height': '',
#         'face': '0',
#         'istype': '2',
#         'qc': '',
#         'nc': '1',
#         'fr': '',
#         'expermode': '',
#         'force': '',
#         'cg': 'girl',
#         'pn': pn,
#         'rn': '30',
#         'gsm': '1e',
#     }
#     page_info = requests.get(url=url, headers=header, params=param)
#     page_info.encoding = 'utf-8'  # 确保解析的格式是utf-8的
#     page_info = page_info.json()  # 转化为json格式在后面可以遍历字典获取其值
#     info_list = page_info['data']  # 观察发现data中存在 需要用到的url地址
#     del info_list[-1]  # 每一页的图片30张，下标是从 0 开始 29结束 ，那么请求的数据要删除第30个即 29为下标结束点
#     img_path_list = []
#     for i in info_list:
#         img_path_list.append(i['thumbURL'])
#         for index in range(len(img_path_list)):
#             print(img_path_list[index])  # 所有的图片的访问地址
#             time.sleep(1)
#             urllib.request.urlretrieve(img_path_list[index],
#                                        "C:/Users/liang/Desktop/solar_panel/" + 'panel_lodge_' + str(n) + '.jpg')
#         n = n + 1
#
#     pn += 29
