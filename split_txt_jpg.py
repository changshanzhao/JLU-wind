import os
import shutil
def mycopyfile(srcfile, dstpath):  # 复制函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.copy(srcfile, dstpath + fname)  # 复制文件
        print("copy %s -> %s" % (srcfile, dstpath + fname))

src = r"D:\JLU-winddata"
f1 = os.listdir(src)
f1_ = []
for i in range(0,len(f1)):
    f1_.append(f1[i].split(".",1))
    if f1_[i][1]=='jpg':
        dst_dir = r"D:\JLU-wind-yolov8\wind-data\images"
        mycopyfile(src+'\\'+f1[i], dst_dir+'\\')
    if f1_[i][1]=='txt':
        dst_dir = r"D:\JLU-wind-yolov8\wind-data\labels"
        mycopyfile(src+'\\'+f1[i], dst_dir+'\\')