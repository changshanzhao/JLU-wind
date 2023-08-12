import pandas as pd
import os
import cv2
src = r"C:\Users\Lenovo\Desktop\dataset-new\dataset-new"
f1 = os.listdir(src+'\\image407-new')
f2 = os.listdir(src+'\\lables407-new')
w = 2000  # 图像宽度
h = 1500  # 图像高度
pan_x = 100  # 设置x偏移量
pan_y = 75   # 设置y偏移量
k = 0  # 计数用的变量
list_l = []  # 存放标签
list_x = []  # 存放原始x
list_y = []  # 存放原始y
list_w = []  # 存放原始w
list_h = []  # 存放原始h
list_pointx = []  # 存放左上角点x
list_pointy = []  # 存放左上角点y
list_width = []  # 存放宽度
list_height = []  # 存放高度
list_newx = []
list_newy = []
list_neww = []
list_newh = []


def get_point(x_, y_, w_, h_):
    x1 = w*x_ - 0.5*w*w_
    y1 = h*y_ - 0.5*h*h_
    return x1, y1

def get_width(w_):
    return w*w_

def get_height(h_):
    return h*h_

if __name__ == '__main__':
    img_test = cv2.imread(src + '\\image407-new\\' + f1[1])
    h, w, _ = img_test.shape
    for i in f2:
        with open(src + '\\lables407-new\\' + f2[k], 'r') as f:
            temp = f.read()
            temp = temp.split()
            n = int(len(temp)/5)
            list_lt = []
            list_xt = []
            list_yt = []
            list_wt = []
            list_ht = []
            for j in range(0, n):
                l_, x_, y_, w_, h_ = eval(temp[0+j*5]), eval(temp[1+j*5]), eval(temp[2+j*5]), eval(temp[3+j*5]), eval(temp[4+j*5])
                list_lt.append(l_)
                list_xt.append(x_)
                list_yt.append(y_)
                list_wt.append(w_)
                list_ht.append(h_)
            list_l.append(list_lt)
            list_x.append(list_xt)
            list_y.append(list_yt)
            list_w.append(list_wt)
            list_h.append(list_ht)
            k += 1
    for i in range(0, 407):
        list_tx = []
        list_ty = []
        list_tw = []
        list_th = []
        for j in range(0, int(len(list_x[i]))):
            tx, ty = get_point(list_x[i][j], list_y[i][j], list_w[i][j], list_h[i][j])
            list_tx.append(tx)
            list_ty.append(ty)
            tw = get_width(list_w[i][j])
            list_tw.append(tw)
            th = get_height(list_h[i][j])
            list_th.append(th)
        list_pointx.append(list_tx)
        list_pointy.append(list_ty)
        list_width.append(list_tw)
        list_height.append(list_th)
    for i in range(0, 407):
        list_tx = []
        list_ty = []
        list_tw = []
        list_th = []
        for j in range(0, int(len(list_x[i]))):
            list_tx.append(list_pointx[i][j]-pan_x)
            list_ty.append(list_pointy[i][j]-pan_y)
            list_tw.append(list_width[i][j]+2*pan_x)
            list_th.append(list_height[i][j]+2*pan_y)
        list_newx.append(list_tx)
        list_newy.append(list_ty)
        list_neww.append(list_tw)
        list_newh.append(list_th)
    # for i in range(0, 5):
    #     cv2.rectangle(img_test,(int(list_newx[1][i]),int(list_newy[1][i])),(int(list_newx[1][i]+list_neww[1][i]),int(list_newy[1][i]+list_newh[1][i])),(255, 0, 0))
    # for i in range(0, 5):
    #     cv2.rectangle(img_test,(int(list_pointx[1][i]),int(list_pointy[1][i])),(int(list_pointx[1][i]+list_width[1][i]),int(list_pointy[1][i]+list_height[1][i])),(0, 255, 0))
    # cv2.namedWindow("windows",cv2.WINDOW_NORMAL)
    # cv2.imshow('windows',img_test)
    # cv2.waitKey(0)



