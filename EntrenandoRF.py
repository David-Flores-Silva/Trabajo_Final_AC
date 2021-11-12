import cv2
import os
import numpy as np

dataPath = ""
peopleList = os.listdir(dataPath)
print("lista de personas: ", peopleList)

labels = []
facesData = []
label = 0

for nameDir in peopleList:
    personPath = dataPath + "/" + nameDir
    print("leyendo las imagenes")

    for fileName in os.listdir((personPath)):
        print("Rostros: ", nameDir + "/" + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath + "/" + fileName, 0))
        image = cv2.imread(personPath + "/" + fileName, 0)

        #cv2.imshow("image", image)
        #cv2.waitkey(10)
    
    label += 1

