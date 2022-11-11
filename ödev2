# İBRAHİM ERKAN 02195076044

# Ters Çevirme

import cv2
import numpy as np

image=cv2.imread("images.jpg",0)
cv2.imshow("orjinal fotograf",image)
cv2.waitKey()

max_photo=np.max(image)

[h,w]=np.shape(image)

for i in range (0,h):
    for j in range (0,w):
        image[i,j]=max_photo-image[i,j]

cv2.imshow("ters fotograf",image)
cv2.waitKey()
