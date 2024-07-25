import cv2

# Read the images
img1 = cv2.imread("images/img1.jpg")
img2 = cv2.imread("images/img2.jpg")

# Resize the images
img1 = cv2.resize(img1, (200, 200))
img2 = cv2.resize(img2, (200, 200))

img_not=cv2.bitwise_not(img1,img2,mask=None)
cv2.imshow("not Image", img_not)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()