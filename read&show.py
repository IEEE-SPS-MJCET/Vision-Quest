import cv2

# Read the images
img1 = cv2.imread("images/img1.jpg")
img2 = cv2.imread("images/img2.jpg")

# Display the first image and print a statement
cv2.imshow("Image 1", img1)
print('khobar')

# Display the second image and print a statement
cv2.imshow("Image 2", img2)
print('flower')

# Wait for a key press and close the image windows yani press q on the images and it will close it
cv2.waitKey(0)
cv2.destroyAllWindows()


