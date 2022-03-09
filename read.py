import cv2 as cv

# img=cv.imread("photo/403022_business man_male_user_avatar_profile_icon.png")
# cv.imshow("fr",img)
# cv.waitKey(0)

capture=cv.VideoCapture("video/dog.mp4")

while True:
    isTrue,frame=capture.read()

    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
capture.destroyAllWindows()