import os.path
from os import path
import os
from collections import OrderedDict
import numpy as np
import itertools
import datetime
import json
#import netCDF4 as nc
import numpy.ma as ma
from PIL import Image
import sys
import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm
import glob

dir_path='../../CVPR_2023_backup'
datapath_b1b4=dir_path+'/b1-b4_train'
datapath_b5b8=dir_path+'/b5-b8_train'
datapath_b9b12=dir_path+'/b9-b12_train'
dataset_b2=glob.glob(datapath_b1b4+'/*B2*')
dataset_b3=glob.glob(datapath_b1b4+'/*B3*')
dataset_b4=glob.glob(datapath_b1b4+'/*B4*')
print(len(dataset_b2))
print(len(dataset_b3))
print(len(dataset_b4))

boundary=['0_255', '256_512', '513_1024','1025_2048', '2049_4096', '4097_8192', '8193_16382','16383_32654','32655_65535','65535_9999999']

original_dataset={'0_255':[], '256_512':[], '513_1024':[],'1025_2048':[], '2049_4096':[], '4097_8192':[], '8193_16382':[],'16383_32654':[],'32655_65535':[],'65535_9999999':[]}
step1={'0_255':[], '256_512':[], '513_1024':[],'1025_2048':[], '2049_4096':[], '4097_8192':[], '8193_16382':[],'16383_32654':[],'32655_65535':[],'65535_9999999':[]}
step2={'0_255':[], '256_512':[], '513_1024':[],'1025_2048':[], '2049_4096':[], '4097_8192':[], '8193_16382':[],'16383_32654':[],'32655_65535':[],'65535_9999999':[]}


def boundary_check(save_dict, name, *args):
    max_=0
    for file in args:
        m=np.max(file)
        if m>max_:
            max_=m 

    for key in boundary:
        start_, end_=key.split('_')[:]
        start, end=int(start_), int(end_)

        if start<=max_<=end:
            save_dict[key].append(name)
            break

for file_path in tqdm(dataset_b2):
    name=file_path.split('/')[-1]
    B2=np.array(Image.open(file_path))
    B3=np.array(Image.open(file_path.replace('B2','B3')))
    B4=np.array(Image.open(file_path.replace('B2','B4')))
    QA60_path=file_path.replace('B2','QA60')
    boundary_check(original_dataset, name, B2, B3, B4)
    ##################step 1.  QA exist , min==max, B2B3B4 > thres#############################
    if path.exists(QA60_path):
        QA60=np.array(Image.open(QA60_path))
        if np.max(QA60)>0:
            continue
    boundary_check(QA60_dict, name, B2, B3, B4)
    
    if np.max(B2)==np.min(B2) or np.max(B3)==np.min(B3) or np.max(B4)==np.min(B4):
        continue

    boundary_check(min_max_dict, name, B2, B3, B4)
    if np.max(B2)>=4096:
        continue
    elif np.max(B3)>=4096:
        continue
    elif np.max(B4)>=4096:
        continue
    boundary_check(step1, name, B2, B3, B4)
    
    ################### step 2. brightness ################################
    img_B2 = ((B2-B2.min())/(B2.max()-B2.min()))*255
    img_B3 = ((B3-B3.min())/(B3.max()-B3.min()))*255
    img_B4 = ((B4-B4.min())/(B4.max()-B4.min()))*255
    img_B2 = np.expand_dims(img_B2, axis=-1)
    img_B3 = np.expand_dims(img_B3, axis=-1)
    img_B4 = np.expand_dims(img_B4, axis=-1)

    img = np.concatenate((img_B4,img_B3,img_B2),axis=-1)
    img = np.array(img,dtype=np.uint8)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    brightness = np.mean(hsv[:,:,2])

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thre = img.shape[0]*img.shape[1]*0.3
    img_gray_T_F = len(img_gray[img_gray<=10])
    if (brightness<30 or img_gray_T_F>thre):
        continue
    boundary_check(step2, name, B2, B3, B4)
    ################### END AND SAVE ################################


with open('original_dataset.json', "w") as json_file:
    json.dump(original_dataset, json_file)
        

with open('step1.json', "w") as json_file:
    json.dump(step1, json_file)

with open('step2.json', "w") as json_file:
    json.dump(step2, json_file)
