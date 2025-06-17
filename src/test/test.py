import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

tracker = cv2.TrackerCSRT_create()
bbox = cv2.selectROI('Tracking', frame, False)
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    success, bbox = tracker.update(frame)

    if success:
        x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    else:
        cv2.putText(frame, "Tracking Failed",
                    (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 1)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
