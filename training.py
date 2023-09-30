import cv2
import numpy as np
from PIL import Image
import os

path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def getImageAndLabels(path):

    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    facesample = []
    ids =[]

    for imagepath in imagePaths:
        PIL_img = Image.open(imagepath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')

        id=int(os.path.split(imagepath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            facesample.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)

    return facesample,ids

print("[INFO] Training Faces....")
faces,ids = getImageAndLabels(path)
recognizer.train(faces, np.array(ids))

recognizer.write('trainer/trainer.yml')

print("[INFO] {0} faces trained.".format(len(np.unique(ids))))

