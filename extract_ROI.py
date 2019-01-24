#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:53:27 2018

@author: asrl
"""

import glob
import cv2
import sys

file_path = sys.argv[1]
out_path = sys.argv[2]
modality = sys.argv[3]

avi_files = sorted(glob.glob(file_path+'*.avi'))
csv_files = sorted(glob.glob(file_path+'*.csv'))
all_files = zip(avi_files,csv_files)
id = 1

for avi,csv in all_files:
    vid_ = cv2.VideoCapture(avi)
    print("Extracting images for id {}".format(id))
    with open(csv,'r') as f:
        a = f.readlines()
    f_stripped = [line.rstrip('\r\n').split(',') for line in a]
    f_stripped.pop(0)
    id_save = "%03d" % id
    im_count = 0
    if 23 < id < 30:
        id += 1
        continue
    else:
        for coords in f_stripped:
            vid_.set(cv2.CAP_PROP_POS_FRAMES,int(coords[0]))
            ret,frame = vid_.read()
            if modality == 'depth':
                frame = cv2.applyColorMap(frame,cv2.COLORMAP_JET)
            roi = frame[int(coords[3]):int(coords[5]),int(coords[2]):int(coords[4]),:]
            im_num = "%03d" % im_count
            cv2.imwrite(out_path+id_save+'/'+im_num+'.png',roi)
            im_count += 1
    id += 1