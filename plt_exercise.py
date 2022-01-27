import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 6, 0.1)        #从0--6以0.1为单位
y1 = np.sin(x)                   #生成sin的图像
y2 = np.cos(x)                   #生成cos的图像

plt.plot(x, y1, label = 'sin')
plt.plot(x, y2, linestyle = '--', label = 'cos')        #用虚线画cos图像
plt.xlabel('x')                 #x轴标签
plt.ylabel('y')                 #y轴标签
plt.title('sin & cos')          #标题
plt.legend()                    #添加图例
plt.show()                      #展示图象（让你看到图像）
