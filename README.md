# labelImgAnnotation_json2yolov5txt
This is the repository about - Conversion of LabelImg Annotation of Json format to yolov5 txt format

## Steps
<br />
<b>Step 1.</b> Clone this repository
<br/>

```shell
git clone https://github.com/shaheera011/labelImgAnnotation_json2yolov5txt.git
```
<br/>

<b>Step 2.</b> Install dependencies
<br/>
```shell
pip install -r requirements.txt
```
<br/>

<b>Step 3.</b> Put All LabelImg Json format Annotations in - labels directory
<br/>
![labels](https://user-images.githubusercontent.com/38965031/176422175-dc77947c-1862-4b24-a09d-0cdd3d8c8134.gif)
<br/>
<br/>

<b>Step 4.</b> Put All Images in - images directory
<br/>
![images](https://user-images.githubusercontent.com/38965031/176422335-1f18fef5-c4ad-4667-956e-d67796785fe0.gif)
<br/>
<br/>

<b>Step 5.</b> Update lut dictonary in (json2yolov5.py) according to your labels names
<br/>
![change_class](https://user-images.githubusercontent.com/38965031/176422740-49cf9b47-939c-407a-91e3-efa30e1e8467.gif)
<br/>
<br/>

<b>[INFO]</b>
<pre>
[Note] Remove requirement.txt & gitignore file from main Directory
</pre>
<br/>

<b>Step 6.</b> Run json2yolov5.py file
<br/>
```shell
python json2yolov5.py
```
<br/>
<br/>

<b>[INFO]</b>
<pre>
[Note] See all your txt format annotations in - Yolov5-labels directory
</pre>
<br/>
