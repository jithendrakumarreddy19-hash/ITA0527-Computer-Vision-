import cv2

img_path = r"C:\Users\jithe\OneDrive\Documents\opencv\images.jpg"

img = cv2.imread(img_path)

lower = (0,0,0)
upper = (120,120,120)

mask = cv2.inRange(img,lower,upper)

result = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("Background",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
