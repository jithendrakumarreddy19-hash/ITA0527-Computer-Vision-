import cv2
import numpy as np

size = int(input("Enter image size: "))

img = np.ones((size,size,3),dtype=np.uint8)*255

cv2.rectangle(img,(50,50),(200,200),(0,255,0),3)

cv2.imshow("Rectangle",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
