import cv2
data = cv2.VideoCapture('./sample.mp4')

while True:
    ret, frame = data.read()
    if ret:
        cv2.imshow('sample data', frame)
        # cv2.waitKey(1)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
    else:
        data.set(cv2.CAP_PROP_POS_FRAMES, 0)

cv2.destroyWindow('sample data')
