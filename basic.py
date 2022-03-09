import cv2 as cv
from cv2 import resize

img=cv.imread("photo/403022_business man_male_user_avatar_profile_icon.png")
cv.imshow("img1",img)
#bgr to gray scale

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("gray",gray)

#blurring the image

blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow("img",blur)

#edge Cascade

canny=cv.Canny(blur,125,175)
cv.imshow("canny",canny)

#Dilating the image
dilated=cv.dilate(canny,(7,7),iterations=5)
cv.imshow("dilated",dilated)

#Eroding

erode=cv.erode(dilated,(3,3,),iterations=3)
cv.imshow("erode",erode)

#resize

resize=cv.resize(img,(300,300),interpolation=cv.INTER_LINEAR)
cv.imshow("resize",resize)

#cropping

crop=img[50:200,200:400]
cv.imshow("crop",crop)


cv.waitKey(0)

