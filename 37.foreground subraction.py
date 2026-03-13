import cv2

img_path = r"C:\Users\jithe\OneDrive\Documents\opencv\images.jpg"

img = cv2.imread(img_path)

lower = (120,120,120)
upper = (255,255,255)

mask = cv2.inRange(img,lower,upper)

result = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("Foreground",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
