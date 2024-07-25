import cv2

# Read the image
img = cv2.imread("images/b&w.png")

# Display the original image
cv2.imshow("before edge detection", img)

# Perform Canny edge detection
edge = cv2.Canny(img, 100, 200)

# Display the edge-detected image
cv2.imshow("after edge detection", edge)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
