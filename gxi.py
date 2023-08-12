"""
Author:zhaojunbo
Date:2023-4-24
"""

# WhiteBalance_set = 2  # 0:close 1:continues 2:once
# Width_set = 640  # 设置分辨率宽
# Height_set = 480  # 设置分辨率高
# framerate_set = 80  # 设置帧率
# # 创建设备
# device_manager = gx.DeviceManager()  # 创建设备对象
# dev_num, dev_info_list = device_manager.update_device_list()  # 枚举设备，即枚举所有可用的设备
# if dev_num is 0:
#     print("Number of enumerated devices is 0")
#     return
# else:
#     print("")
#     print("**********************************************************")
#     print("创建设备成功，设备号为:%d" % dev_num)
# # 通过设备序列号打开一个设备
# cam = device_manager.open_device_by_sn(dev_info_list[0].get("sn"))
# # 设置宽和高
# cam.Width.set(Width_set)
# cam.Height.set(Height_set)
# # 设置帧率
# cam.AcquisitionFrameRate.set(framerate_set)
# # 设置连续采集
# cam.AcquisitionFrameRateMode.set(gx.GxSwitchEntry.ON)
# # 设置白平衡
# cam.BalanceWhiteAuto.set(WhiteBalance_set)
# w = Width_set
# h = Height_set
# cam.stream_on()
# self.fps[i] = cam.CurrentAcquisitionFrameRate.get()
# self.frames[i] = max(int(cam.GetTotalFrameCount()), 0) or float('inf')  # infinite stream fallback
# raw_image = cam.data_stream[0].get_image()
# rgb_image = raw_image.convert("RGB")
# numpy_image = rgb_image.get_numpy_array()
import gxipy as gx
from PIL import Image
import datetime
import cv2
"""
Author:NoamaNelson
Date:2019-11-21
Discription:Secondary development of pythonsdk of Daheng camera.
"""


def main():
    Width_set = 640  # 设置分辨率宽
    Height_set = 480  # 设置分辨率高
    framerate_set = 80  # 设置帧率
    num = 5  # 采集帧率次数（为调试用，可把后边的图像采集设置成while循环，进行无限制循环采集）

    # 打印
    print("")
    print("###############################################################")
    print("               连续获取彩色图像并显示获取的图像.")
    print("###############################################################")
    print("")
    print("摄像机初始化......")
    print("")

    # 创建设备
    device_manager = gx.DeviceManager()  # 创建设备对象
    dev_num, dev_info_list = device_manager.update_device_list()  # 枚举设备，即枚举所有可用的设备
    if dev_num is 0:
        print("Number of enumerated devices is 0")
        return
    else:
        print("")
        print("**********************************************************")
        print("创建设备成功，设备号为:%d" % dev_num)

    # 通过设备序列号打开一个设备
    cam = device_manager.open_device_by_sn(dev_info_list[0].get("sn"))

    # 如果是黑白相机
    if cam.PixelColorFilter.is_implemented() is False:  # is_implemented判断枚举型属性参数是否已实现
        print("该示例不支持黑白相机.")
        cam.close_device()
        return
    else:
        print("")
        print("**********************************************************")
        print("打开彩色摄像机成功，SN号为：%s" % dev_info_list[0].get("sn"))

    # 设置宽和高
    cam.Width.set(Width_set)
    cam.Height.set(Height_set)

    # 设置连续采集
    # cam.TriggerMode.set(gx.GxSwitchEntry.OFF) # 设置触发模式
    cam.AcquisitionFrameRateMode.set(gx.GxSwitchEntry.ON)

    # 设置帧率
    cam.AcquisitionFrameRate.set(framerate_set)
    print("")
    print("**********************************************************")
    print("用户设置的帧率为:%d fps" % framerate_set)
    framerate_get = cam.CurrentAcquisitionFrameRate.get()  # 获取当前采集的帧率
    print("当前采集的帧率为:%d fps" % framerate_get)

    # 开始数据采集
    print("")
    print("**********************************************************")
    print("开始数据采集......")
    print("")
    cam.stream_on()

    # 采集图像
    for i in range(num):
        raw_image = cam.data_stream[0].get_image()  # 打开第0通道数据流
        if raw_image is None:
            print("获取彩色原始图像失败.")
            continue

        rgb_image = raw_image.convert("RGB")  # 从彩色原始图像获取RGB图像
        if rgb_image is None:
            continue

        # rgb_image.image_improvement(color_correction_param, contrast_lut, gamma_lut)  # 实现图像增强

        numpy_image = rgb_image.get_numpy_array()  # 从RGB图像数据创建numpy数组
        if numpy_image is None:
            continue

        img = Image.fromarray(numpy_image, 'RGB')  # 展示获取的图像
        # img.show()
        mtime = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')

        img.save(r"D:\image\\" + str(i) + str("-") + mtime + ".jpg")  # 保存图片到本地

        print("Frame ID: %d   Height: %d   Width: %d   framerate_set:%dfps   framerate_get:%dfps"
              % (raw_image.get_frame_id(), raw_image.get_height(), raw_image.get_width(), framerate_set,
                 framerate_get))  # 打印采集的图像的高度、宽度、帧ID、用户设置的帧率、当前采集到的帧率

    # 停止采集
    print("")
    print("**********************************************************")
    print("摄像机已经停止采集")
    cam.stream_off()

    # 关闭设备
    print("")
    print("**********************************************************")
    print("系统提示您：设备已经关闭！")
    cam.close_device()


if __name__ == "__main__":
    main()


""" 
def main():
    
    Width_set = 640 # MAX:1280
    Height_set = 480 # MAX:1080
    framerate_set = 80 
    OffsetX_set = 0
    OffsetY_set = 28
    WhiteBalance_set = 2 # 0:close 1:continues 2:once
    num = 1    
    print("**********************************************************")
    device_manager = gx.DeviceManager() 
    dev_num, dev_info_list = device_manager.update_device_list() 
    if dev_num is 0:
        print("Number of enumerated devices is 0")
        return
    else:
        print("")
        #print("**********************************************************")
        print("create success dev_num:%d" % dev_num)
    
    cam = device_manager.open_device_by_sn(dev_info_list[0].get("sn"))

    if cam.PixelColorFilter.is_implemented() is False: 
        print("no support")
        cam.close_device()
        return
    else:
        print("")
        #print("**********************************************************")
        print("success open colored cam, sn:%s" % dev_info_list[0].get("sn"))

    cam.Width.set(Width_set)
    cam.Height.set(Height_set)
    cam.OffsetX.set(OffsetX_set)
    cam.OffsetY.set(OffsetY_set)
    print("")
    print("**********************************************************")
    print("Resolution Setting: (Width_MAX:1280 Height_MAX:1080)")
    print("")
    print("Width:%d Height:%d" % (Width_set,Height_set))
    print("")
    print("Offset X:%d Offset Y:%d" % (OffsetX_set,OffsetY_set))
    print("**********************************************************")
    cam.BalanceWhiteAuto.set(WhiteBalance_set)
    print("")
    print("WhiteBalance Setting: (0:close 1:continues 2:once)")
    print("")
    print("Mode:%d" % WhiteBalance_set)

    cam.AcquisitionFrameRateMode.set(gx.GxSwitchEntry.ON)
    cam.AcquisitionFrameRate.set(framerate_set)
    print("")
    print("**********************************************************")
    print("frame per sec:%d fps"%framerate_set)
    framerate_get = cam.CurrentAcquisitionFrameRate.get() 
    print("capture fps:%d fps"%framerate_get)


    print("")
    print("**********************************************************")
    print("start capture")
    print("")
    cam.stream_on()
    while True:
        for i in range(num):
            raw_image = cam.data_stream[0].get_image() 
            if raw_image is None:
                print("fail to get colored image")
                continue

            rgb_image = raw_image.convert("RGB")
            if rgb_image is None:
                continue

            #rgb_image.image_improvement(color_correction_param, contrast_lut, gamma_lut) 

            numpy_image = rgb_image.get_numpy_array()
            if numpy_image is None:
                continue
            numpy_image = cv2.cvtColor(numpy_image,cv2.COLOR_RGB2BGR)
            #img = Image.fromarray(numpy_image, 'RGB') 
            cv2.imshow("frame",numpy_image)
            if cv2.waitKey(1) & 0xFF == ord('s'):
            	mtime = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
            	cv2.imwrite('/home/nvidia/Desktop/photos/'+ str(mtime) + '.jpg', numpy_image) 
            	print("Frame ID: %d   Height: %d   Width: %d   framerate_set:%dfps   framerate_get:%dfps"
              	  % (raw_image.get_frame_id(), raw_image.get_height(), raw_image.get_width(), framerate_set, framerate_get)) 
        if cv2.waitKey(1) & 0xFF == 27:
            break

    print("")
    print("**********************************************************")
    print("cam stop")
    cam.stream_off()

    print("")
    print("device closed")
    print("**********************************************************")
    cam.close_device()

if __name__ == "__main__":
    main()
"""
