import cv2
import numpy as np

img = cv2.imread(r"C:\Users\jithe\OneDrive\Documents\opencv\images.jpg", 0)
kernel = np.ones((5, 5), np.uint8)

_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

cv2.imshow("Original", binary)
cv2.imshow("Opening", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()