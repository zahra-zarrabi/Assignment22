import cv2
import numpy as np

images=[]
for i in range(14):
    image=cv2.imread(f'image/highway/h{i}.jpg')
    image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    images.append(image)
img_result=np.zeros(images[0].shape,dtype="uint8")
for image in images:
    img_result += image // len(images)

cv2.imwrite("highway.jpg",img_result)
cv2.imshow("show output",img_result)
cv2.waitKey()
