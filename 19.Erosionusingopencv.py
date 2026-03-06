import cv2
import numpy as np

# Read image
img = cv2.imread(r'C:\Users\jithe\OneDrive\Documents\opencv\images.jpg')

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Erosion Image", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()