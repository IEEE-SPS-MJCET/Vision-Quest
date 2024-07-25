import cv2
import numpy as np

# Read the images
img1 = cv2.imread("images/25.jpg")
img2 = cv2.imread("images/24.jpg")

# Display the images
cv2.imshow("Image 1", img1)
print('flowers')
cv2.imshow("Image 2", img2)
print('something random')

# Resize the images
img1 = cv2.resize(img1, (500, 200))
img2 = cv2.resize(img2, (500, 200))

# Subtract the images
img_sub = cv2.subtract(img1, img2)

# Display the subtracted image
cv2.imshow("Subtracted Image", img_sub)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
