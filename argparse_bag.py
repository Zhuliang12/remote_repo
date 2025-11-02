# 机   构：上海海事大学
#  开发人： 朱亮
# 开发时间：2022/12/8 16:17

import argparse  # 导入包
import math


def parse_args():
    parse = argparse.ArgumentParser(description='Calculate cylinder volume')  # 创建参数对象
    parse.add_argument('radius', type=int, default=2, help='Radius of Cylinder')  # 往参数对象中加入参数
    # parse.add_argument('-r','--radius',default=2,type=int,help='radius of cylinder')
    # 在参数名前，加入‘-’,变成可以选引用名，简化命令行输入
    # parse.add_argument('--radius',default=2,type=int,help='radius of cylinder')
    #  在参数名前加入“--”变成可以选参数，没有输入就会使用default值，不然就是None
    # 清除帮助中的参数名信息
    # parse.add_argument('-r', '--radius', default=2, type=int, metavar='', help='')
    # 这里设置为空，不显示
    # 设置必选参数
    # parse.add_argument('-r','--radius',default=2,type=int,metavar='',required=True,help='')
    # 当设置了required=True ,无论是否是可选参数都必须输入
    parse.add_argument('height', type=int, default=2, help='height of Cylinder')
    # 默认参数设置
    # parse.set_defaults(height=4)
    # set_defaults可以设置一些参数的默认值 default 系统设置
    args = parse.parse_args()  # 解析参数对象获得解析对象
    return args


# 列表参数传入设置
def parse_args1():
    parse = argparse.ArgumentParser(description='calculate cylinder volume')
    parse.add_argument('-n', '--num', default=2, type=int, metavar='', required=True, help='')
    '''
    # 在参数对象中添加一组互斥组
    group=parse.add_mutually_exclusive_group()
    # 在互斥组中添加参数（store_true)默认当命令行来输入参数为False,否则为True
    group.add_argument('-b','--brief',action='store_true',help='')
    group.add_argument('-v','--verbose',action='store_true',help='')
    # 这里 b和v,只能输入其中一个参数
    '''
    opt = parse.parse_args()  # 解析参数对象获得解析对象
    return opt


def cal_vol(radius, height):  # 计算圆柱体积
    vol = math.pi * pow(radius, 2) * height
    return vol


if __name__ == '__main__':
    args = parse_args()
    print(cal_vol(args.radius, args.height))  # 使用解析对象，参数获取使用命令行参数
