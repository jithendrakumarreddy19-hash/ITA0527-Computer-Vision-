import cv2

img = cv2.imread(r'C:\Users\jithe\OneDrive\Documents\opencv\images.jpg')

# Crop small ROI
roi = img[10:60, 10:60]

# Paste ROI nearby
img[70:120, 70:120] = roi

cv2.imshow("Image", img)
cv2.imshow("ROI", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()