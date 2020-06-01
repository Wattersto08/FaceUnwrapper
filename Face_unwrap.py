import cv2
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image

vidcap = cv2.VideoCapture('IMG_8485.mp4')
success,image = vidcap.read()
count = 0

print('Reading MP4 File')
while success: 
    cv2.imwrite("frame%d.jpg" % count, image[0:1920,535:545])     # save frame as JPEG file 
#    print(image.shape)
    success,image = vidcap.read()
    #print('Read a new frame: ', success)
    count += 1


print('cutting and pasting the images!')
finim = Image.open("frame1.jpg")
for i in range(count):
    im = Image.open("frame%d.jpg" % i)
    imarray = np.array(im)
    finim = np.hstack((finim,im))

img = Image.fromarray(finim, 'RGB')
img.save('Unwrapped_face.png')
#img.show()

files_in_directory = os.listdir()
print('clean up time!')
for file in files_in_directory:
    if file.endswith(".jpg"):
       # print(file)
        os.remove(file)

print('Done, enjoy!')
