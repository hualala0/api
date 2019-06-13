import os
import torch
import numpy as np
import cv2
import pandas as pd

from myapp.loadimage.crowd_count import CrowdCounter
from myapp.loadimage import network


def cc(img):
    net = CrowdCounter()
    trained_model = os.path.join('myapp/networks/mcnn_shtechA_38.h5')
    network.load_net(trained_model, net)
    net.cuda()
    net.eval()
    img = img.astype(np.float32, copy=False)
    print(img.shape)
    ht = img.shape[0]
    wd = img.shape[1]
    ht_1 = int((ht/4)*4)
    wd_1 = int((wd/4)*4)
    img = cv2.resize(img,(wd_1,ht_1))
    img = img.reshape((1,1,img.shape[0],img.shape[1]))
    im_data = img
    density_map = net(im_data)
    density_map = density_map.data.cpu().numpy()
    et_count = density_map
    return np.sum(et_count)
