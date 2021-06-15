import cv2

image_origin=cv2.imread('image/board - origin.bmp')
image_test=cv2.imread('image/board - test.bmp')

image_origin=cv2.cvtColor(image_origin,cv2.COLOR_RGB2GRAY)
image_test=cv2.cvtColor(image_test,cv2.COLOR_RGB2GRAY)
image_test=cv2.flip(image_test,1)

image_result=cv2.subtract(image_test,image_origin)*4

cv2.imshow('show output',image_result)
cv2.waitKey()