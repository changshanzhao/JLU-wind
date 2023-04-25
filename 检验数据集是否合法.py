import pandas as pd
import os
src = r"E:\YOLOwind\wind-data\labels"
f1 = os.listdir(src+'\\train')
f2 = os.listdir(src+'\\val')
for i in f1:
    data = pd.read_csv('wind-data/labels/train'+'\\'+i,
                       names=['class', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x5', 'y5'],
                       header=None, sep=" ")
    t=data['class']
    for p in t:
        if(p>5 or p<0):
            print(i)

for j in f2:
    data = pd.read_csv('wind-data/labels/val'+'\\'+j,
                       names=['class', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x5', 'y5'],
                       header=None, sep=" ")
    t=data['class']
    for q in t:
        if(q>5 or q<0):
            print(j)
