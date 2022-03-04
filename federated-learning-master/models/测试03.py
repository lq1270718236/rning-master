#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : face_prepare.py
# @Author: WangYe
# @Date  : 2019/4/17
# @Software: PyCharm

from PIL import Image
import numpy as np
import random

def LDPData(image_dir):
    #image_dir = r"C:\Users\DELL\Desktop\个人论文\实验测试.jpg"
    #x = Image.open(image_dir)  # 打开图片
    x=image_dir
    data = np.array(x)  # 转换为矩阵
    juzhen=data.shape
    #print(juzhen)  # 输出矩阵
    ch=juzhen[0]
    ka=juzhen[1]
    se=juzhen[2]
    #print("11111111111111111111111111111111111111111111111111111")
    for i in range (ch/6):
        for j in range(ka/6):
            x=random.randint(0,ch-1)
            y = random.randint(0,ka-1)
            m=data[x][y]
            c = random.randint(0, se - 1)
            #print(m[c])
            #print("21892732974038")
            tttt = ldp(m[c])
            #print(tttt)
            m[c]=tttt

    image = Image.fromarray(data)
    '''image.show()# 将之前的矩阵转换为图片
    print("2222222222222222222222222222222222222222222222222222222")
      # 调用本地软件显示图片，win10是叫照片的工具
    #print("3333333333333333333333333333333333333333333333333333333")'''
    return (image)

def ldp(shuzi):
    while True:
        b = []  # 定义一个空数组，用于存放2整除后的商
        while True:
            b.append(str(shuzi % 2))  # 用列表的append方法追加
            shuzi = shuzi // 2  # 用地板除求num的值
            if shuzi == 0:  # 若地板除后的值为0，那么退出循环
                break
        #print(b)
        for i in range(2 * 3):#k=3
            nt = random.randint(0, len(b) - 1)
            # print(nt)
            if b[nt] != 0:
                b[nt] = 0
            else:
                b[nt] = 1
        decimal_number = 0
        for j in range(len(b)):
            decimal_number += int(b[j]) * pow(2, j)
        if decimal_number <= 255:
            break
    return(decimal_number)



#LDPData()