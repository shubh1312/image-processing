import cv2

video=cv2.VideoCapture(0)
a=0
while True:
    a+=1
    check,frame = video.read()
    print(frame)

    cv2.imshow('firstFrame',frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()