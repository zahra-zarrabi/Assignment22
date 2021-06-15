import cv2
import numpy as np

Mona_Lisa=cv2.imread('image/Mona_Lisa.jpg')
b=cv2.imread('image/yellow.tif')
Mona_Lisa=cv2.cvtColor(Mona_Lisa,cv2.COLOR_RGB2GRAY)
b=cv2.cvtColor(b,cv2.COLOR_RGB2GRAY)

img_result = Mona_Lisa/b

cv2.imshow("Show output",img_result)
cv2.imwrite("Mona_Lisa.jpg",img_result*255)
cv2.waitKey()
