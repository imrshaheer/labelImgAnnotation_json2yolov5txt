# -*- coding: utf-8 -*-

import json
import os
import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
import shutil

lut={}
lut["2_3_Axel_Truck"] = 0
lut["Articulated_Vehicle"]  = 1
lut["Buses"] = 2
lut["Car_Jeep"]  = 3
lut["Coaster_MiniBus"]  = 4
lut["Van_Wagon"]  = 5

ROOT_DIR = os.getcwd()
# print(ROOT_DIR)
jsonLabels_dir = ROOT_DIR + "\labels"
images_dir = ROOT_DIR + "\images"

def moveFile(txt_labels):
    txt_labels_path = txt_labels
    # print(txt_labels_dir)
    isExists = os.path.join(txt_labels_path + "\yolov5-labels")

    if not os.path.exists(isExists):
        os.makedirs(isExists)
        os.chdir(os.path.join("yolov5-labels"))
        destination_dir = os.getcwd()

        txtFiles =[]

        for filename in os.listdir(txt_labels_path):
            if filename.endswith(".txt"):
                txtFiles.append(filename)

        for txt in txtFiles:
            shutil.move(os.path.join(txt_labels_path, txt), os.path.join(destination_dir, txt))

# box form[x,y,w,h]
def normalized2Yolov5(size, box):

    dw = size[1]
    dh = size[0]
    x = (box[0]) / dw
    y = (box[1]) / dh
    w = (box[2]) / dw
    h = (box[3]) / dh

    return (x, y, w, h)

def getValues(jsonObj):

    for x in jsonObj:
        # print(x)
        # imageName = x["image"]
        annotations = x["annotations"]
        # print("\n\n",len(annotations))
        Bbox = []
        for ann in annotations:
            labelName = ann["label"]
            coords = ann["coordinates"]
            cx = coords["x"]
            cy = coords["y"]
            width = coords["width"]
            height = coords["height"]

            line = [str(labelName), str(cx), str(cy), str(width), str(height)]
            Bbox.append(line)
            
    return Bbox

def convert_json2yolo( jsonLabels_dir ):
    # step into dataset directory
    DIRS = jsonLabels_dir
    # print(DIRS)

    for fileName in tqdm(os.listdir(DIRS)):
        # print(fileName)
        file1 = open(os.path.join(DIRS, fileName))
        jsonObj = json.load(file1)
        image_path = os.path.join(images_dir + f"\{fileName[:-5]}.jpg" )
        # print(path)
        img = cv2.imread(image_path)
        size = img.shape[:-1]
        # print(size)
        Bbox = getValues(jsonObj)
        # print(Bbox)
        annotations = []
        for b in Bbox:
            labels = np.array(b)
            class_name = labels[0]
            class_name = lut[class_name]

            coords = np.asarray([round(float(labels[1]), 6), round(float(labels[2]), 6), round(float(labels[3]), 6), round(float(labels[4]), 6)])

            coords = normalized2Yolov5(size, coords)
            # print(coords)
            labels[1], labels[2], labels[3], labels[4] = coords[0], coords[1], coords[2], coords[3]
            newline = str(class_name) + " " + str(labels[1]) + " " + str(labels[2]) + " " + str(labels[3]) + " " + str(labels[4])
            # print(newline)

            annotations.append(newline)

        fileName = fileName[:-5] + '.txt'


        with open(fileName, "w") as outfile:
            for line in annotations:
                outfile.write(line)
                outfile.write("\n")
            outfile.close()

    moveFile(txt_labels= ROOT_DIR)


def main():
    convert_json2yolo( jsonLabels_dir )

if __name__ == '__main__':
    main()