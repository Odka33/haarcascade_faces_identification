import cv2
import numpy as np
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost:5432",
    database="measurements",
    user="exploit",
    password="exploit123"
)
cursor = conn.cursor()

# Load the cascade for face detection
face_cascade = cv2.CascadeClassifier(r"C:\Users\benay\Downloads\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml")

# Load the image
img = cv2.imread('image_01.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Iterate over the faces
for (x, y, w, h) in faces:
    # Extract the face
    face = img[y:y+h, x:x+w]
    gray_face = gray[y:y+h, x:x+w]

    # Detect the eyes
    eyes = cv2.CascadeClassifier(r"C:\Users\benay\Downloads\opencv\sources\data\haarcascades\haarcascade_eye.xml")
    eyes = eyes.detectMultiScale(gray_face)

    # Calculate the average distance between the eyes
    eye_distance = 0
    for (ex,ey,ew,eh) in eyes:
        eye_distance += ex + ew/2
    eye_distance /= len(eyes)

    # Detect the mouth
    mouth = cv2.CascadeClassifier(r"C:\Users\benay\Downloads\opencv\sources\data\haarcascades\haarcascade_mcs_mouth.xml")
    mouth = mouth.detectMultiScale(gray_face)

    # Classify the mouth shape
    mouth_shape = 'undetermined'
    for (mx,my,mw,mh) in mouth:
        if mw > 0.5 * w and mh > 0.15 * h:
            mouth_shape = 'smiling'
        else:
            mouth_shape = 'neutral'

    # Detect the nose
    nose = cv2.CascadeClassifier(r"C:\Users\benay\Downloads\opencv\sources\data\haarcascades\haarcascade_mcs_nose.xml")
    nose = nose.detectMultiScale(gray_face)

    # Classify the nose shape
    nose_shape = 'undetermined'
    for (nx,ny,nw,nh) in nose:
        if nw > 0.3 * w and nh > 0.3 * h:
            nose_shape = 'big'
        else:
            nose_shape = 'small'

    # Detect the cheekbones
    cheekbones = cv2.CascadeClassifier(r"C:\Users\benay\Downloads\opencv\sources\data\haarcascades\haarcascade_")
    cheekbones = cheekbones.detectMultiScale("gray_face")

    # Calculate the average height of the cheekbones
    cheekbone_height = 0
    for (cx,cy,cw,ch) in cheekbones:
        cheekbone_height += cy + ch/2
        cheekbone_height /= len(cheekbones)

# Store the face measurements in the database
cursor.execute("INSERT INTO measurements (eye_distance, mouth_shape, nose_shape, cheekbone_height) VALUES (?,?,?,?)", (eye_distance, mouth_shape, nose_shape, cheekbone_height))
conn.commit()

# Close the database connection
conn.close()
