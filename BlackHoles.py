import cv2
import numpy as np

images=[[0 for i in range(5)] for j in range(4)]
for i in range(4):
    for j in range(5):
        images[i][j]=cv2.imread(f'image/black_hole/{i+1}/{j+1}.jpg')
        images[i][j]=cv2.cvtColor(images[i][j],cv2.COLOR_BGR2GRAY)
        images[i][j] = cv2.resize(images[i][j], (500, 500))


image_without_noise=[0 for i in range(4)]
for i in range(4):
    for j in range(5):
        image_without_noise[i] += images[i][j]/5

img_result=np.zeros((1000,1000),dtype="uint8")
img_result[0:500, 0:500] = image_without_noise[0]
img_result[0:500, 500:1000] = image_without_noise[1]
img_result[500:1000, 0:500] = image_without_noise[2]
img_result[500:1000, 500:1000] = image_without_noise[3]

cv2.imwrite("result.jpg",img_result)
cv2.imshow("show output",img_result)
cv2.waitKey()