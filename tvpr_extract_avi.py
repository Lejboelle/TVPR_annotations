import glob
import cv2
import sys
import os

g001 = [1,2,3,4,2,4,3,1]
g002 = [5,6,7,5,7,6]
g003 = [8,9,9,8]
g004 = [10,11,12,11,12,10]
g005 = [13,14,15,16,15,13,16,14]
g006 = [17,18,19,20,21,22,23,21,19,17,23,20,22,18]
g007 = [24,25,26,27,28,29,28,27,29,26,24,25]
g008 = [30,31,32,31,32,30]
g009 = [33,34,35,36,34,36,35,33]
g010 = [37,38,39,40,41,42,41,42,39,37,40,38]
g011 = [43,44,45,46,47,46,44,47,43,45]
g012 = [48,49,50,51,52,53,54,52,54,50,53,48,49,51]
g013 = [55,56,57,58,59,60,59,57,60,55,58,56]
g014 = [61,62,63,64,65,64,62,65,61,63]
g015 = [66,67,68,69,70,71,71,68,66,69,67,70]
g016 = [72,73,74,75,75,73,74,72]
g017 = [76,77,78,79,80,79,77,80,76,78]
g018 = [81,82,83,82,83,81]
g019 = [84,85,86,87,88,87,85,84,88,86]
g020 = [89,90,91,92,91,89,92,90]
g021 = [93,94,93,94]
g022 = [95,96,97,96,95,97]
g023 = [98,99,100,100,98,99]

registrations = [g001,g002,g003,g004,g005,g006,g007,g008,g009,g010,g011,g012,g013,g014,g015,g016,g017,g018,g019,g020,g021,g022,g023]

pwd_ = sys.argv[1]
modality = sys.argv[2]
avi_files = sorted(glob.glob(pwd_+"/avi_"+modality+"/*.avi"))
annotations = []
anot_path = pwd_+'tvpr_frame_count.txt'
anot_file = open(anot_path,'r')

for line in anot_file:
    annotations.append(line.split(' '))

ids = zip(*annotations)
train_path = pwd_+"/train/"
test_path = pwd_+"/test/"
train_rgb = []
test_rgb = []
train_d = []
test_d = []
id_count = 0
fourcc = cv2.VideoWriter_fourcc(*'X264')
height = 480
width = 640

for i in range(len(registrations)):
 #   if i != 6:
        rec_ids = list(set(registrations[i]))
        cur_ids = [annotations[index-1] for index in rec_ids]
        avi = avi_files[i]
        cap = cv2.VideoCapture(avi)
        assert cap.isOpened(), \
        'Cannot open file'
        fps = round(cap.get(cv2.CAP_PROP_FPS))

        for sub_id in cur_ids:
        ## Extract train frames
            print("Processing id {}" .format(sub_id[0]))
            train_count = 0
            test_count = 0
            id_fold = "%03d" % int(sub_id[0])
            videoWriter1 = cv2.VideoWriter(pwd_+'/tracking_files/'+modality+'/train/output_train_{}.avi'.format(id_fold), fourcc, fps, (width, height))
            videoWriter2 = cv2.VideoWriter(pwd_+'/tracking_files/'+modality+'/test/output_test_{}.avi'.format(id_fold), fourcc, fps, (width, height))
            for m in range(int(sub_id[1]),int(sub_id[2])):
                cap.set(cv2.CAP_PROP_POS_FRAMES,m) 
                ret, img = cap.read()
                videoWriter1.write(img)
                train_count += 1
        
        ## Extract test frames
            for n in range(int(sub_id[3]),int(sub_id[4])):
                cap.set(cv2.CAP_PROP_POS_FRAMES,n) 
                ret, img = cap.read()
                videoWriter2.write(img)
                test_count += 1
            videoWriter1.release()
            videoWriter2.release()
            id_count += 1 

