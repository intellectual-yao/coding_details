#include <opencv2\opencv.hpp>
#include <iostream>
#include <cstring>
#include<stdio.h>
#include<stdlib.h>
#include <time.h>

using namespace cv;
using namespace std;


int main()
{
    int n = 20,pos_x,pos_y;
    Mat img = imread("C:\\Users\\intellectual_yao\\Desktop\\pic\\model_m\\src.jpg");
    string save_path = "E:\\new_apps\\ViT\\dianluban\\new_data\\";
    Mat ROI1;
    srand((int)time(0));
    while (n < 29){
        pos_x = int(rand() % 7000);//生成随机数，本人图片大小7000*9344
        pos_y = int(rand() % 9344);
        if (pos_x + 224 <= 7000 && pos_y + 224 <= 9344)
        {
            ROI1 = img(Rect(pos_x, pos_y, 224, 224));//输出图片大小224*224
            string path = save_path + to_string(n) + ".jpg";
            imwrite(path, ROI1);
            n++;
        }
    }
    return 0;
}
