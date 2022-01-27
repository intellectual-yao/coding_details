import cv2
import os
import numpy as np
from skimage import transform, data
import matplotlib.pyplot as plt


# 依次读取文件夹的所有图片
def read_directory(dir_path):
    k = 15
    # C:\Users\intellectual_yao\Desktop\pic\new_resize
    new_path = "E:\\new_apps\\ViT\\dianluban\\resize_data\\after_deal"
    for img_name in os.listdir(dir_path):
        print(img_name)
        # 读图
        _img = cv2.imread(dir_path + "\\" + img_name)
        print(_img.shape)

        # resize_img = cv2.resize(_img, (512, 512))
        # print(resize_img.shape)

        v_image = cv2.flip(_img, 0)  # 图像垂直翻转
        resize_v_img = cv2.resize(v_image, (512, 512))
        print("resize_v_img.shape is: ", resize_v_img.shape)
        k += 1
        save_path = new_path + "\\" + str(k) + ".jpg"
        cv2.imwrite(save_path, resize_v_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

        h_image = cv2.flip(_img, 1)  # 图像水平翻转
        resize_h_img = cv2.resize(h_image, (512, 512))
        print("resize_h_img.shape is: ", resize_h_img.shape)
        k += 1
        save_path = new_path + "\\" + str(k) + ".jpg"
        cv2.imwrite(save_path, resize_h_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

        h_v_image = cv2.flip(_img, -1)  # 图像垂直和水平翻转.
        resize_h_v_img = cv2.resize(h_v_image, (512, 512))
        print("resize_h_v_img.shape is: ", resize_h_v_img.shape)
        k += 1
        save_path = new_path + "\\" + str(k) + ".jpg"
        cv2.imwrite(save_path, resize_h_v_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])


# 对处理后的图进行二值化
def threshold_pic(dir_path):
    for img_name in os.listdir(dir_path):
        print(img_name)
        # 读图
        _img = cv2.imread(dir_path + "\\" + img_name)
        _, bi_img = cv2.threshold(_img, 120, 255, cv2.THRESH_BINARY)
        cv2.namedWindow("bi_img", 0)
        cv2.imshow("bi_img", bi_img)
        cv2.waitKey(0)


def deal_pic(pic):
    # 处理图
    # v_image = cv2.flip(pic, 0)  # 图像垂直翻转
    #
    # h_image = cv2.flip(pic, 1)  # 图像水平翻转
    #
    # h_v_image = cv2.flip(pic, -1)  # 图像垂直和水平翻转
    #
    # cv2.namedWindow("v_image", 0)
    # cv2.imshow("v_image", v_image)
    # cv2.namedWindow("h_image", 0)
    # cv2.imshow("h_image", h_image)
    # cv2.namedWindow("h_v_image", 0)
    # cv2.imshow("h_v_image", h_v_image)
    cv2.waitKey(0)

if __name__ == '__main__':
    # C:\Users\intellectual_yao\Desktop\pic\new_pic\1.jpg
    dir_path = "E:\\new_apps\\ViT\\dianluban\\resize_data\\resize_data"
    # one_path = "E:\\xiangmu\\BSrc1Not.jpg"
    # read_one(dir_path)

    read_directory(dir_path)
    # threshold_pic(dir_path)

