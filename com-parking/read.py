import cv2
car_cascade=cv2.CascadeClassifier('cars.xml')
img=cv2.imread('car3.jpg')
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cars=car_cascade.detectMultiScale(imggray,1.1,4)
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
