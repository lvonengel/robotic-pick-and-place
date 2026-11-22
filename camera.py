import cv2
import time

#opens the first camera
cap = cv2.VideoCapture(0)
time.sleep(1)

#grab frame
success, image = cap.read()
if success:
    cv2.imwrite("test.jpg", image)
    print(f'size: {image.shape}')
else:
    print("Could not read camera")

cap.release()