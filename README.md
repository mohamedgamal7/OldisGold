# Old but gold !
## Old but gold !
## Haar cascade classifier (OpenCV)

This repo is an implementation of the famous Haar cascade classifier using opencv.This piece of work was done long before the Deep Learning Era had even started. But it’s an excellent work in comparison to the powerful models that can be built with the modern day Deep Learning Techniques. The algorithm is still found to be used almost everywhere. 

# Haar cascase under the hood 

## what is Haar Cascade? 
 
It is an Object Detection Algorithm used to identify faces in an image or a real time video. The algorithm uses edge or line detection features proposed by Viola and Jones in their research paper “Rapid Object Detection using a Boosted Cascade of Simple Features” published in 2001. The algorithm is given a lot of positive images consisting of faces, and a lot of negative images not consisting of any face to train on them. 


## Features

The Haar cascade is a machine learning technique so features are needed to be well defined before training. The features shown above make it easy to find out the edges or the lines in the image, or to pick areas where there is a sudden change in the intensities of the pixels.



The objective here is to find out the sum of all the image pixels lying in the darker area of the haar feature and the sum of all the image pixels lying in the lighter area of the haar feature. And then find out their difference. Now if the image has an edge separating dark pixels on the right and light pixels on the left, then the haar value will be closer to 1. That means, we say that there is an edge detected if the haar value is closer to 1. In the example above, there is no edge as the haar value is far from 1.
 
## Reducing calculations 

### Integral image 

An Integral Image is calculated from the Original Image in such a way that each pixel in this is the sum of all the pixels lying in its left and above in the Original Image. The calculation of a pixel in the Integral Image can be seen in the above GIF. The last pixel at the bottom right corner of the Integral Image will be the sum of all the pixels in the Original Image.

### Adaboost
a Boosting Technique called AdaBoost was used, In which each of these 180,000 features were applied to the images separately to create Weak Learners. Some of them produced low error rates as they separated the Positive images from the Negative images better than the others, while some didn’t. These weak learners are designed in such a way that they would misclassify only a minimum number of images. They can perform better than only a random guess. With this technique, their final set of features got reduced to a total of 6000 from 180,000 features.

## Attentional Cascade

Now comes the Cascading part. The subset of all 6000 features will again run on the training images to detect if there’s a facial feature present or not. Now the authors have taken a standard window size of 24x24 within which the feature detection will be running. It’s again a tiresome task.

To simplify this, they proposed another technique called The Attentional Cascade. The idea behind this is, not all the features need to run on each and every window. If a feature fails on a particular window, then we can say that the facial features are not present there. Hence, we can move to the next windows where there can be facial features present.

Features are applied on the images in stages. The stages in the beginning contain simpler features, in comparison to the features in a later stage which are complex, complex enough to find the nitty gritty details on the face. If the initial stage won’t detect anything on the window, then discard the window itself from the remaining process, and move on to the next window. This way a lot of processing time will be saved, as the irrelevant windows will not be processed in the majority of the stages.
The second stage processing would start, only when the features in the first stage are detected in the image. The process continues like this, i.e. if one stage passes, the window is passed onto the next stage, if it fails then the window is discarded.


## Steps

`cmd: python face_taker.py`

 Take pictures using the `face_taker.py` script. The script will save 30 images of your face in the `images` folder after you entered the ID number (MUST be integer and incremental (starts with 1 then 2, 3, ...)
Note: Make sure your face is centered. The window will collapse when all the 30 pictures are taken.

`cmd: python face_taker_img.py`

This script takes a path to a directory and reads images that are already their to be used for training the haar cascade classifier, the directory named `mo` has 30 images of Mohamed salah for this purpose.


`cmd: python face_train.py`

The `face_train.py` script will train a model to recognize all the faces from the 30 images taken using `face_taker.py` script, and save the training output in the `training.yml` file.


`cmd: python face_recognizer.py`

 The `face_recognizer.py` is the main script. You need to append the name of each person who sees his/her picture taken in the `face_taker.py` script. The program will recognize the face according to the id given in the `face_taker.py` script. If Joe has an id 1, his name should appear in the list as index 1 like this `names = ['None', 'Joe'] # keep None and append a name into this list`

## Requirements:

- `pip install opencv-python`
- `pip install opencv-contrib-python --upgrade` or `pip install opencv-contrib-python --user`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
