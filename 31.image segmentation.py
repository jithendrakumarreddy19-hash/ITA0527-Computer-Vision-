import cv2

img_path = r"C:\Users\jithe\OneDrive\Documents\opencv\images.jpg"

img = cv2.imread(img_path,0)

ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow("Original",img)
cv2.imshow("Segmented",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
