# TVPR_annotations
The repository provides Top View Person Re-identification (TVPR) annotations and corresponding guide to extract ROI images. 

Before following the guide below, make sure you have downloaded the dataset (http://vrai.dii.univpm.it/re-id-dataset) and video files are in ".avi" format. Split the videos into two folders in your TVPR root folder. Name these folders "avi_color" and "avi_depth", respectively.

Additionally, before running the scripts, create the following directories in your root folder:
train/
test/
tracking_files/depth/train/
tracking_files/depth/test/
tracking_files/color/train/
tracking_files/color/test/

Finally, for each id, create directories that will contain the final ROI images, similar to the example below:
train/roi_images/color/001/
train/roi_images/color/002/
.
.
train/roi_images/color/100/

Directories should be created also in case of color test and depth train/test images, following a similar structure.

## Annotation information
Annotations are extracted using the You Only Look Once (YOLO) detector (REF). \
Two types of annotations are provided: \
(1) "tvpr_frame_count.txt" contains information on frame numbers for each video which contains a person in the scene. Should be placed in the TVPR root folder. \
(2) For each extracted ".avi" file (both RGB and depth, train and test), a corresponding ".csv" file is created, containing ROI coordinates for each frame. Each ".csv" file contains a list of annotations, each providing five numbers: \
frame_id - frame number in the video \
track_id - always '1', does not have any effect \
xmin - left coordinate of bounding box \
ymin - top coordinate of bounding box \
xmax - right coordinate of bounding box \
ymax - bottom coordinate of bounding box \

## Extract relevant part of videos
First, only the relavant parts of the avi files contained in the dataset are extracted to separate avi files.
This is accomplished by running the following command, once for each modality:
```shell
python tvpr_extract_avi.py [ROOT_PATH] [MODALITY]
```
where [ROOT_PATH], naturally, is the path to your TVPR root folder and [MODALITY] should be 'color' or 'depth'.
This will create minor ".avi" files in the "tracking_files" sub-directories.

## Extracting ROI images
Before running the script to extract ROI images, place the ".csv" files from this repository to respective subdirectories in your "tracking_files" folder. \
To extract the ROI images, run the following command, in total, four times (depth train, depth test, color train, color test):
```shell
python extract_ROI.py [AVI/CSV PATH] [OUTPUT_PATH] [MODALITY]
```

where [AVI/CSV PATH] is, for example, the path "tracking_files/depth/test", [OUTPUT_PATH] is the path to save in the ROI images, for example, "train/roi_images/color/" (without id folder) and [MODALITY] is 'color' or 'depth'. \
Please note that we exclude id's 23-30, as a result, images from 94 id's are available.

Training and test ROI images should now be extracted and ready to use for training.
