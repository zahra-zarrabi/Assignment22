import cv2

a=cv2.imread('image/a.tif')
b=cv2.imread('image/b.tif')

a=cv2.cvtColor(a,cv2.COLOR_RGB2GRAY)
b=cv2.cvtColor(b,cv2.COLOR_RGB2GRAY)

img_result=cv2.add(b,a)

cv2.imwrite("image.jpg",img_result)
cv2.imshow('show output',img_result)
cv2.waitKey()