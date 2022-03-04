from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random

from blinker import base

import ldp
img1 = Image.open(r"C:\Users\DELL\Desktop\个人论文\论文实验图\未命名文件.jpg")

img2 = Image.open(r"C:\Users\DELL\Desktop\个人论文\论文实验图\延伸图.png")

'''img2.paste(img1, (0, 0))

img2.paste(img1, (600, 300, 600 + img1.size[0], 300 + img1.size[1]))

img2.paste((0, 0, 255), (0, 600, 100, 700))'''

im2arr = np.array(img1)
print(im2arr)# im2arr.shape: height x width x channel
'''for m in range(1332):
    for n in range(2043):
     im2arr[m][n]=250
for m in range(1332 // 60):
    m1 = random.randint(0, 1330)
    for n in range(2043 // 60):
        n1 = random.randint(0, 2040)
        a = im2arr[m1][n1]
        #list = [a >> d & 1 for d in range(10)][::-1]
        while True:
            b=[]
            while True:  # 一直循环，商为0时利用break退出循环
                s = a // 2  # 商
                y = a % 2  # 余数
                b = b + [y]  # 每一个余数存储到b中
                if any(s == 0):
                    break  # 余数为0时结束循环
                a = s
            b.reverse()  # 使b中的元素反向排列
            b = [str(p) for p in b ]
            #b = ['0b'] + b
            print(b)
            b = []  # 定义一个空数组，用于存放2整除后的商
            while True:
                b.append(str(a % 2))  # 用列表的append方法追加
                a = a // 2  # 用地板除求num的值
                if a == 0:  # 若地板除后的值为0，那么退出循环
                    break
            print(b)
            for i in range(2 * 3):
                nt = random.randint(0, len(b)-1)
                #print(nt)
                if any(b[nt])!= 0:
                    b[nt] = 0
                else:
                    b[nt] = 1
            decimal_number = 0
            for j in range(len(b)):
                decimal_number += int(b[j]) * pow(2, j)
            if decimal_number <= 255:
                break
        im2arr[m1][n1] = decimal_number
#image = Image.fromarray(im2arr)
img2 = Image.fromarray(im2arr)


plt.imshow(img2)

plt.show()'''