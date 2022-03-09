import cv2 as cv
import numpy as np
from pyparsing import col

blank=np.ones((500,500,3),dtype='uint8')
cv.imshow('blank',blank)

blank[100:300]=0,0,255
cv.imshow('blank',blank)
img=cv.imread("photo/403022_business man_male_user_avatar_profile_icon.png")

cv.imshow("img",img)

#rectangle

cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)
cv.imshow("rect",blank)

#circle
cv.circle(blank,(250,250),40,(0,200,0),thickness=cv.FILLED)
cv.imshow("rect",blank)

#lines
cv.line(blank,(0,0),(250,250),(255,255,255))
cv.imshow("line",blank)


#text
cv.putText(img,"hello",(250,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0))
cv.imshow("line",img)

cv.waitKey(0)