import cv2
cat_cascade = cv2.CascadeClassifier('./cascade.xml')
data = cv2.VideoCapture('./sample.mp4')

while True:
    ret, frame = data.read()
    if ret:
        gray_data = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detect = cat_cascade.detectMultiScale(gray_data)
        for x, y, w, h in detect:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('sample data', frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        data.set(cv2.CAP_PROP_POS_FRAMES, 0)

cv2.destroyWindow('sample data')
