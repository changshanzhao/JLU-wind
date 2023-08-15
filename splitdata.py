# 不报错的话运行一次就就好
import os
import random
import shutil

def moveFile(val_img_Dir, val_mask_Dir):
        iamge_src_dir = r"E:\YOLOwind\wind-data\images"
        label_src_dir = r"E:\YOLOwind\wind-data\labels"
        img_pathDir = os.listdir(iamge_src_dir)                    # 提取图片的原始路径
        img_pathDir.remove('train')
        img_pathDir.remove('val')
        filenumber = len(img_pathDir)

        # 自定义val的数据比例
        val_rate = 0.2
        val_picknumber = int(filenumber*val_rate)                  # 按照val_rate比例从文件夹中取一定数量图片

        # 选取移动到val中的样本
        sample2 = random.sample(img_pathDir, val_picknumber)
        print(sample2)
        for i in range(0, len(sample2)):
            sample2[i] = sample2[i][:-4]
        for name in sample2:
            dst_img_name = val_img_Dir + '\\' + name
            dst_txt_name = val_mask_Dir + '\\' + name
            shutil.move(iamge_src_dir + '\\' + name + '.jpg', dst_img_name + '.jpg')
            shutil.move(label_src_dir + '\\' + name + '.txt', dst_txt_name + '.txt')
        return

if __name__ == '__main__':
    # train 目录
    train_img_Dir = r"E:\YOLOwind\wind-data\images\train"
    train_mask_Dir = r"E:\YOLOwind\wind-data\labels\train"
    # val路径：图片和标注文目录
    val_img_Dir = r"E:\YOLOwind\wind-data\images\val"
    val_mask_Dir = r"E:\YOLOwind\wind-data\labels\val"
    # 运行划分数据集函数,把一部分移动到val里面
    moveFile(val_img_Dir, val_mask_Dir)
    # 最后自己手动把剩下的拷贝到train文件夹里吧，懒得写了，后续或许更新
