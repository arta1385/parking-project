import cv2
img=cv2.imread('car.jpg')
imgblur=cv2.blur(img,(3,3))
cv2.imshow('car',img)
cv2.imshow('carblur',imgblur)
cv2.waitKey(0)
