import pandas as pd
import os
src = r"E:\YOLOwind\wind-data\labels"
f1 = os.listdir(src+'\\train')
f2 = os.listdir(src+'\\val')
for i in f1:
    data = pd.read_csv('wind-data/labels/train'+'\\'+i,
                       names=['class', 'x', 'y', 'w', 'h', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5'],
                       header=None, sep=" ")
    data.drop(columns=['x', 'y', 'w', 'h'], inplace=True)
    data.to_csv('wind-data/labels/train'+'\\'+i, sep=' ', index=0, header=0)
for j in f2:
    data = pd.read_csv('wind-data/labels/val'+'\\'+j,
                       names=['class', 'x', 'y', 'w', 'h', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5'],
                       header=None, sep=" ")
    data.drop(columns=['x', 'y', 'w', 'h'], inplace=True)
    data.to_csv('wind-data/labels/val'+'\\'+j, sep=' ', index=0, header=0)