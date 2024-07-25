import cv2
import matplotlib.pyplot as plt

img=cv2.imread('images/b&w.png')
img = cv2.resize(img, (200, 200))
cv2.imshow("histogram",img)

#find frequency of pixels in range 0-255
#syntax: cv2.calcHist(images, channels, mask, histsize, ranges)
hist = cv2.calcHist([img],[1],None,[250],[0,250])

#plotting graph
plt.plot(hist)
plt.show()
