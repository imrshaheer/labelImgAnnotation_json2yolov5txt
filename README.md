# labelImgAnnotation_json2yolov5txt
This is the repository about - Conversion of LabelImg Annotation of Json format to yolov5 txt format

## Steps
<br />
<b>Step 1.</b> Clone this repository: https://github.com/shaheera011/labelImgAnnotation_json2yolov5txt.git
<br/>
<br/>

<b>Step 2.</b> Install dependencies
<pre>
pip install -r requirements.txt
</pre>
<br/>

<b>Step 3.</b> Put All LabelImg Json format Annotations in - labels directory
<br/>
![labels](https://user-images.githubusercontent.com/38965031/176422175-dc77947c-1862-4b24-a09d-0cdd3d8c8134.gif)
<br/>

<b>Step 4.</b> Put All Images in - images directory
<br/>
![images](https://user-images.githubusercontent.com/38965031/176422335-1f18fef5-c4ad-4667-956e-d67796785fe0.gif)
<br/>

<b>Step 5.</b> Update lut dictonary in (json2yolov5.py) according to your labels names
![change_class](https://user-images.githubusercontent.com/38965031/176422740-49cf9b47-939c-407a-91e3-efa30e1e8467.gif)
<br/>

<b>Step 6.</b> Run json2yolov5.py file
<pre>
python json2yolov5.py
</pre>
<br/>

<b>Step 7.</b> [INFO]
<pre>
[Note] See all your txt format annotations in - Yolov5-labels directory
</pre>
<br/>
