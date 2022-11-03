import cv2
import numpy as np

# İBRAHİM ERKAN 02195076044

img = cv2.imbread("ari.jpg", 0)
cv2.imshow("not inverter", img)
x = img.shape[0]
y = img.shape[1]
img2 = np.zeros([x, y], dtype=np.uint8)

for i in range(x):
    for j in range(y):
        img2[i,j] = 225 - img[i,j]

cv2.imshow("inverter", img2)
cv2.waitKey()
