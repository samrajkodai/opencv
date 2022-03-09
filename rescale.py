from turtle import heading
import cv2 as cv

#resizing function

def rescale_frame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimesion=(width,height)

    return cv.resize(frame,dimesion,interpolation=cv.INTER_AREA)


# capture=cv.VideoCapture("video/dog.mp4")

# while True:
#     isTrue,frame=capture.read()
#     frame_resized=rescale_frame(frame,0.15)
#     cv.imshow('video',frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('s'):
#         break


# capture.release()
# capture.destroyAllWindows()


#images

img=cv.imread("photo/403022_business man_male_user_avatar_profile_icon.png")


cv.imshow("fr",img)

resized_image=rescale_frame(img)
cv.imshow("resize",resized_image)
cv.waitKey(0)