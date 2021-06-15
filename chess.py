import cv2

img_chess=cv2.imread('image/chess pieces.jpg')

img_chess=cv2.cvtColor(img_chess,cv2.COLOR_RGB2GRAY)

(thresh,img_binary)=cv2.threshold(img_chess, 170, 255, cv2.THRESH_BINARY)

column = []
obj = False
for n in range(img_binary.shape[1]):
    if not obj:
        if any(img_binary[:, n] != 255):
            column.append(n)
            obj = True
    else:
        if all(img_binary[:, n] == 255):
            column.append(n)
            obj = False
for m in range(0, len(column), 2):
    cv2.imwrite(f"result{m}.jpg",img_chess[:, column[m]:column[m+1]])

cv2.imshow("show output",img_binary)
cv2.waitKey()