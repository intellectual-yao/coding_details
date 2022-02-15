import cv2
import os
from PIL import Image, ImageChops, ImageEnhance
import skimage
import numpy as np
from skimage import transform, data
import matplotlib.pyplot as plt


# 依次读取文件夹的所有图片
def read_directory(dir_path):
    k = 30
    # C:\Users\intellectual_yao\Desktop\pic\new_resize
    new_path = "E:\\new_apps\\ViT\\dianluban\\else\\received_new"
    for img_name in os.listdir(dir_path):
        print(img_name)
        # 读图
        _img = cv2.imread(dir_path + "\\" + img_name)
        print(_img.shape)

        # resize_img = cv2.resize(_img, (512, 512))
        # print(resize_img.shape)

        v_image = cv2.flip(_img, 0)  # 图像垂直翻转
        # resize_v_img = cv2.resize(v_image, (512, 512))
        # print("resize_v_img.shape is: ", resize_v_img.shape)
        k += 1
        save_path = new_path + "\\" + str(k) + ".jpg"
        cv2.imwrite(save_path, v_image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

        h_image = cv2.flip(_img, 1)  # 图像水平翻转
        # resize_h_img = cv2.resize(h_image, (512, 512))
        # print("resize_h_img.shape is: ", resize_h_img.shape)
        k += 1
        save_path = new_path + "\\" + str(k) + ".jpg"
        cv2.imwrite(save_path, h_image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

        h_v_image = cv2.flip(_img, -1)  # 图像垂直和水平翻转.
        # resize_h_v_img = cv2.resize(h_v_image, (512, 512))
        # print("resize_h_v_img.shape is: ", h_v_image.shape)
        k += 1
        save_path = new_path + "\\" + str(k) + ".jpg"
        cv2.imwrite(save_path, h_v_image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

        h, w = _img.shape[:2]
        center = (w // 2, h // 2)
        # 旋转中心坐标，逆时针旋转：45°，缩放因子：1.1
        M_1 = cv2.getRotationMatrix2D(center, 45, 1.1)
        rotated_1 = cv2.warpAffine(_img, M_1, (w, h))
        k += 1
        save_path = new_path + "\\" + str(k) + ".jpg"
        cv2.imwrite(save_path, rotated_1, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])


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


# 加高斯噪声，平移图片（循环移位）PIL库，因此部分代码需替换
def move_img(dir_path):
    k = 132
    new_path = "E:\\new_apps\\ViT\\dianluban\\else\\moved_without_gap"
    for img_name in os.listdir(dir_path):
        print(img_name)
        img_path = dir_path + "\\" + img_name
        _img = Image.open(img_path)
        moved_img = ImageChops.offset(_img, 100, 150)
        k += 1
        save_path = new_path + "\\" + str(k) + ".jpg"
        moved_img.save(save_path)

        # img = np.array(_img) # 分类任务，本数据集加噪声以后变为全黑，故不能使用加噪DA
        # img_noise = skimage.util.random_noise(img, mode="gaussian")
        # k += 1
        # save_path = new_path + "\\" + str(k) + ".jpg"
        # cv2.imwrite(save_path, img_noise, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
        # plt.imshow(img)
        # plt.show()


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
    dir_path = "E:\\new_apps\\ViT\\dianluban\\else\\received_new"
    # one_path = "E:\\xiangmu\\BSrc1Not.jpg"
    # read_one(dir_path)

    # read_directory(dir_path)
    # threshold_pic(dir_path)
    move_img(dir_path)

