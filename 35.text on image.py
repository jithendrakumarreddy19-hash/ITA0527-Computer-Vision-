import cv2

img_path = r"C:\Users\jithe\OneDrive\Documents\opencv\images.jpg"

img = cv2.imread(img_path)

text = input("Enter text: ")

cv2.putText(img,text,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

cv2.imshow("Text Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
