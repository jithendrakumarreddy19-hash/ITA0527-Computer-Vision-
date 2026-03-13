import cv2

video_path = r"C:\Users\jithe\OneDrive\Documents\opencv\3320517-hd_720_1280_25fps.mp4"

cap = cv2.VideoCapture(video_path)

car_cascade = cv2.CascadeClassifier(r"C:\Users\jithe\OneDrive\Documents\opencv\cars.xml")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
