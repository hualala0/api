# coding=gbk
from PIL import Image
import numpy as np


# import scipy
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def loadImage(im):
    # 读取图片
    im = im.convert("L")
    #im.show()
    im = im.resize((28, 28), Image.ANTIALIAS)
    data = im.getdata()
    data = np.matrix(data)
    data = np.reshape(data, (28, 28))
    return  data

def rtnY(data,w,w_h):
    x = data.reshape(-1, 1)
    h_value = np.dot(w, x)  # 线性输出
    h_output = sigmoid(h_value)
    output_value = np.dot(w_h, h_output)
    y = sigmoid(output_value)
    return np.argmax(y)

