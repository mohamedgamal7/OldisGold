import numpy as np
import cv2
import os

if not os.path.exists('images'):
    os.makedirs('images')

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input('\n enter user id (MUST be an integer) and press <return> -->  ')

count = 0
enum = 1
for filename in os.listdir("mo"):
    print("\n [INFO] Reading image {}/30 from directory ".format(enum))
    enum+=1
    img = cv2.imread(os.path.join("mo", filename))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1
        # Save the captured image into the images directory
        cv2.imwrite("./images/Users." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
        cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff
        if k < 30:
            break
cv2.destroyAllWindows()