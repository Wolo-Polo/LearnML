'''
Created on Mar 27, 2020

@author: Truong

Bài toán đặt ra: dùng hồi quy tuyến tính để dự đoán điểm thi của sinh viên
input: danh sách điểm kiểm tra lần 1, 2, 3 và điểm thi của sinh viên (dữ liệu train)
điểm lần 1, 2, 3 của sinh viên cần dự đoán điểm thi
output: điểm thi dự đoán của sinh viên

Giả sử y=F(w) là 1 hàm tuyến tính: y=w0+w1*x0+w2*x1+w3*x2
Hàm mất mát: L(w)=....
Mục tiêu: tính w=? để L(w) min
Đạo hàm L(w) theo w: l(x)=Xbar.T*(Xbar*w-y)

'''
import numpy as np
#import matplotlib.pyplot as plt

#dữ liệu train
X= np.array([[73, 93, 89, 96, 73, 53, 69, 47, 87, 79, 69, 70, 93, 79, 70, 93, 78, 81, 88, 78, 82, 86, 78, 76, 96],
            [80, 88, 91, 98, 66, 46, 74, 56, 79, 70, 70, 65, 95, 80, 73, 89, 75, 90, 92, 83, 86, 82, 83, 83, 93],
            [75, 93, 90, 100, 70, 55, 77, 60, 90, 88, 73, 74, 91, 73, 78, 96, 68, 93, 86, 77, 90, 89, 85, 71, 95]]).T

y= np.array([[152, 185, 180, 196, 142, 101, 149, 115, 175, 164, 141, 141, 184, 152, 148, 192, 147, 183, 177, 159, 177, 175, 175, 149, 192]]).T

# xây dựng Xbar
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

# tính w
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ', w)


def F(w, x0, x1, x2):
    return w[0][0] + w[1][0]*x0 + w[2][0]*x1 + w[3][0]*x2


#lấy giá trị ban đầu
w = np.array([[1], [1], [1], [1]])
alpha=0.01

#nhập dữ liệu dự đoán
x0=float(input("diem lan 1?\n"))
x1=float(input("diem lan 2?\n"))
x2=float(input("diem lan 3?\n"))

diemthi=F(w, x0, x1, x2)
print("diem thi du kien: %0.2f" %diemthi)
