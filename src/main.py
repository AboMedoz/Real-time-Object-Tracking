import cv2


def object_tracker():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    tracker = cv2.TrackerCSRT_create()
    bbox = cv2.selectROI("ROI", frame, False)
    tracker.init(frame, bbox)

    while True:
        ret, frame = cap.read()
        success, bbox = tracker.update(frame)

        if success:
            x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3]),
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Tracking Failed", (100, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))

        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
    cap.release()


if __name__ == "__main__":
    object_tracker()