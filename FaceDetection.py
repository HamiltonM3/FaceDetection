import numpy as np
import cv2

image_files = ['face.jpg', 'face2.jpg', 'face3.jpg']

pretrained = 'haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier(pretrained)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

for image in image_files:
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(40,40))

    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2) #red bounding box

    eyes = eye_cascade.detectMultiScale(gray)

    for (ex, ey, ew, eh) in eyes:
        # Get the region of interest
        roi = img[ey:ey+eh, ex:ex+ew]
        # Apply the blur
        blur = cv2.medianBlur(roi, 55)
        # Replace the original region with blurred region
        img[ey:ey+eh, ex:ex+ew] = blur

    cv2.imshow('face_detected',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
