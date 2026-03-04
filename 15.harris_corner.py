import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\jithe\OneDrive\Documents\opencv\images.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Harris corner detection
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Mark corners in red
img[corners > 0.01 * corners.max()] = [0,0,255]

# Show image
cv2.imshow("Harris Corners", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
