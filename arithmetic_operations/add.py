import cv2

# Read the images
img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")

# Resize images to the same size
img1 = cv2.resize(img1, (300, 400))
img2 = cv2.resize(img2, (300, 400))

# Addition of images
img_add = cv2.add(img1, img2)

# Display the added image
cv2.imshow("Added Image", img_add)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()