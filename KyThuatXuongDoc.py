'''
Created on Mar 21, 2020

@author: Truong
'''
#f(x)=x*x+5*sin(x)
#tìm x sao cho f(x) min bằng kĩ thuật xuống dốcs

import random
import numpy as np
import matplotlib.pyplot as plt


def F(x):
    return x*x+5*np.sin(x)

#đây là đạo hàm của  F(x) theo x
def f(x):
    return 2*x+5*np.cos(x)
    
def mini(x, alpha):
    for i in range(10000):
        x=x-alpha*f(x)
    return x

#lấy tốc độ học đủ nhỏ
alpha=0.01
#lấy ngẫu nhiên điểm x ban đầu
x= random.randint(-1000, 1000)
minx=mini(x, alpha)
minf=F(minx)
print('Gia tri cua x ban dau: '+str(x))
print('Cuc tieu dia phuong: '+str(minx))
print('Gia tri cuc tieu dia phuong: '+str(minf))

Ox= [_ for _ in range(int(minx)-10, int(minx)+10)]
Oy= [F(x) for x in Ox]

print(Ox)
print(Oy)
plt.plot(Ox, Oy)
plt.plot(minx, minf, 'ro')
plt.show()