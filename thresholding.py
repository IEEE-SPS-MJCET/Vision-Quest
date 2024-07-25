import cv2

# Step 1: Read the image in grayscale mode
# This converts the image to black and white shades
img = cv2.imread("images/BalloonRed.png", cv2.IMREAD_GRAYSCALE)

# Step 2: Display the original grayscale image
cv2.imshow("Original Image", img)

# Step 3: Apply simple binary thresholding
# If a pixel value is greater than 127, it's set to 255 (white), otherwise, it's set to 0 (black)
threshold_value = 127
max_value = 255
_, thresh_img = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_BINARY)

# Step 4: Display the thresholded image
cv2.imshow("Thresholded Image", thresh_img)

# Step 5: Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
