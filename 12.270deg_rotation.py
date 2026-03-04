import cv2

# Read image
img = cv2.imread(r"C:\Users\jithe\OneDrive\Documents\opencv\images.jpg")

# Rotate 270 degrees clockwise
rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Show image
cv2.imshow("Original Image", img)
cv2.imshow("270 Degree Rotation", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
