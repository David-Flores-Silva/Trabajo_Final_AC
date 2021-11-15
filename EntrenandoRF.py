import cv2
import os
import numpy as np

dataPath = "D:/DAVID/UNSA/IV TAREAS/9. labo de AC/Trabajo_Final_AC/Data"
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

#print("labels: ",labels)
#print("numero de etiquetas 0: ",np.count_nonzero(np.array(labels)==0))
#print("numero de etiquetas 0: ",np.count_nonzero(np.array(labels)==1))
 

#face_recognizer = cv2.face.EigenFaceRecognizer_create()
face_recognizer = cv2.face.FisherFaceRecognizer_create()
 
print("entrenamiento ... ")
face_recognizer.train(facesData, np.array(labels))
 

#face_recognizer.write("modeloEigenFace.xml")
face_recognizer.write("modeloFisherFace.xml")
print("modelo almacenado")
