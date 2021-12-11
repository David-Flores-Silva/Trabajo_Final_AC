import cv2
import os
#from main import alumno1
 
dataPath = "D:/DAVID/UNSA/IV TAREAS/9. labo de AC/Trabajo_Final_AC/Data"
imagePaths = os.listdir(dataPath)
print("imagePaths= ", imagePaths)
personPath = "Briana"

#face_recognizer = cv2.face.EigenFaceRecognizer_create()
face_recognizer = cv2.face.FisherFaceRecognizer_create()
 
#leendo el modelo
#face_recognizer.read("modeloEigenFace.xml")
face_recognizer.read("modeloFisherFace.xml")
 
#cap = cv2.VideoCapture("img y videos/Clara.mp4")
cap = cv2.VideoCapture("img y videos/"+personPath+".mp4")
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
 
while True:
    ret, frame = cap.read()
    if ret == False:
        break
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()
 
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)
 
    for (x, y, w, h) in faces:
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation = cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)
 
        cv2.putText(frame, "{}".format(result),(x,y-10),1,1.3,(0,255,0),1,cv2.LINE_AA)
 
        #1
        #if result[1] < 5700:
        #    cv2.putText(frame, "{}".format(imagePaths[result[0]]),(x,y+5),1,1.3,(0,255,0),1,cv2.LINE_AA)
        #    cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), 2)
        #else:
        #    cv2.putText(frame, "Desconocido",(x,y+5),1,1.3,(0,0,255),1,cv2.LINE_AA)
        #    cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 0, 255), 2)
    
        #2
        if result[1] < 500:
            cv2.putText(frame, "{}".format(imagePaths[result[0]]),(x,y-30),1,1.3,(255,198,26),2,cv2.LINE_AA)
            cv2.putText(frame, "{}".format("Asistencia Registrada"),(x-100,y+220), 1,1.8, (255, 255, 0), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,198,26), 2)
            print("se registro la asistencia de: "+personPath)
            #for i in range(len(alumno1)-1):
             #   if alumno1[i].name == personPath:
              #      alumno1[i].asistencia = True
        else:
            cv2.putText(frame, "Desconocido",(x,y-30),1,1.3,(0,0,255),1,cv2.LINE_AA)
            cv2.putText(frame, "{}".format(result),(x,y-10),1,1.3,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 0, 255), 2)
 
 
 
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
 
cap.release()
cv2.destroyAllWindows()