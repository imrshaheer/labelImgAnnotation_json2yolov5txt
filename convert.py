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

image_file_extension = ".jpg"


ROOT_DIR = os.getcwd()

labels_dir = ROOT_DIR + "\\labels"
images_dir = ROOT_DIR + "\\images"


def main(labels_dir, images_dir):

    annotations = []

    for file in tqdm(os.listdir(labels_dir)):
        
        txt_file_name = str(file).split(".")[0] + '.txt'
        
        image_name = str(file).split(".")[0]
        image_path = os.path.join(images_dir + f"\\{image_name}" + image_file_extension )
        image = cv2.imread(image_path)
        image_size = image.shape[:-1]

        with open(os.path.join(labels_dir, file), 'r') as file:
            file = json.load(file)
            bbox = getValues(file)
        
        for box in bbox:
            cls = box[0]
            cords = np.asarray([float(box[1]), 
                                float(box[2]), 
                                float(box[3]), 
                                float(box[4])])
            
            x, y, w, h = normalized2Yolov5(image_size, cords)

            newline = str(cls) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)

            annotations.append(newline)
        
        with open(txt_file_name, "w") as f:
            for line in annotations:
                f.write(line)
                f.write("\n")
            f.close()

    moveFile(txt_files_path=ROOT_DIR)
            

def getValues(file):

    for x in file:
        annotations = x["annotations"]
        Bbox = []
        for ann in annotations:
            cls = ann["label"]
            cls = lut[cls]
            cords = ann["coordinates"]
            cx = cords["x"]
            cy = cords["y"]
            width = cords["width"]
            height = cords["height"]

            line = [str(cls), str(cx), str(cy), str(width), str(height)]
            Bbox.append(line)
            
    return Bbox


def normalized2Yolov5(size, box):

    dw = size[1]
    dh = size[0]
    x = (box[0]) / dw
    y = (box[1]) / dh
    w = (box[2]) / dw
    h = (box[3]) / dh

    return x, y, w, h  


def moveFile(txt_files_path):

    isExists = os.path.join(txt_files_path + "\\yolotxt_labels")
    
    if not os.path.exists(isExists):
        os.makedirs(isExists)
        os.chdir(os.path.join("yolotxt_labels"))

        destination_dir = os.getcwd()
        print(destination_dir)

        txt_files =[]

        for filename in os.listdir(txt_files_path):
            if filename.endswith(".txt"):
                txt_files.append(filename)

        for txt in txt_files:
            shutil.move(os.path.join(txt_files_path, txt), os.path.join(destination_dir, txt))
    else:
        print("[INFO] Please delete [yolotxt_labels] folder first!!!")


if __name__ == '__main__':
    main(labels_dir, images_dir)