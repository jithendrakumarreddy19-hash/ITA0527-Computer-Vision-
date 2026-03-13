import cv2
import numpy as np

size = int(input("Enter image size: "))

img = np.ones((size,size,3),dtype=np.uint8)*255
box = size//10

img[0:box,0:box] = (0,0,0)
img[0:box,size-box:size] = (255,0,0)
img[size-box:size,0:box] = (0,255,0)
img[size-box:size,size-box:size] = (0,0,255)

cv2.imshow("Boxes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
