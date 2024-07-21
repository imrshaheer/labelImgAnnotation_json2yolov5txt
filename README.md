
# Convert Annotation Project - LabelImg JSON Format to Yolo TXT Format 

Welcome to the Conversion of (LabelImg Annotation of Json format) to (Yolo txt format)
## Summary

This project demonstrates a conversion of annotation format, from lableimg json format to yolo txt format.
















## Features

- Convert Annotation Format.
- LabelImg Json Format to Yolo Txt Format.
- And Move all the Yolo Txt format files to specific folder.



## Steps

#### Step 1. Clone this repository

```shell
git clone https://github.com/shaheera011/labelImgAnnotation_json2yolov5txt.git
```

#### Step 2. Install dependencies

#### Step 3. Put All LabelImg Json format Annotations in - labels Directory

![labels](https://user-images.githubusercontent.com/38965031/176422175-dc77947c-1862-4b24-a09d-0cdd3d8c8134.gif)


#### Step 4. Put all your Images in (images) directory

![images](https://user-images.githubusercontent.com/38965031/176422335-1f18fef5-c4ad-4667-956e-d67796785fe0.gif)

#### Step 5. Update lut dictonary in (convert.py) according to your labels names

![change_class](https://user-images.githubusercontent.com/38965031/176422740-49cf9b47-939c-407a-91e3-efa30e1e8467.gif)

### Step 6. Run convert.py file

```shell
python json2yolov5.py
```

#### [Note] See all your txt format annotations in - Yolov5-labels directory




## Authors

- [@imrshaheer](https://www.github.com/imrshaheer)

