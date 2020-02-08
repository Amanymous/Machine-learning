import cv2
img=cv2.imread("/home/aman/Documents/opencv/puppy.jpeg")

while True:
    cv2.imshow("puppy",img)
    #if we wait at least 1 ms AND we have pressed the Esc
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyALLWindows()