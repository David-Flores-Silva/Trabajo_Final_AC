from datetime import datetime
from Alumno import Alumno
from Curso import Curso
#from Confiabilidad import Variable_principal
import smtplib
import getpass




#--------------------           TIME            ------------#

print(datetime.now().strftime("%H:%M:%S"))
hora = datetime.now().strftime("%H:%M:%S").split(sep=":")
for hor in hora:
    print(hor)

#--------------------           TIME            ------------#


#Colegio New School (7 alumnos)

alumno1 = []
alumno1.append(Alumno(20202131, "Adriano", 6))
alumno1.append(Alumno(20202132, "Briana", 12))
alumno1.append(Alumno(20202133, "Hanna", 12))
alumno1.append(Alumno(20202134, "Juliana", 6))
alumno1.append(Alumno(20202135, "Luana", 8))
alumno1.append(Alumno(20202136, "Pablo", 12))
alumno1.append(Alumno(20202137, "Sophia", 13))

ColegioNS = Curso("Colegio New School", "07:30:00", "08:15:00", "NewSchool@gmail.com", alumno1)
print(ColegioNS)


#for alum in alumno1:
#    if(Variable_principal):
#        alum.asistencia == True

message = ""
for i in range(len(alumno1)-1):
    message = message + str(alumno1[i])


#--------------------           CORREO            ------------#

subject = "Asistencia_1"
message = "Subject: {}\n\n{}".format(subject, message)

password = getpass.getpass("ingrese contraseña: ")
server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()
server.login("cchadavid12@gmail.com", password)
server.sendmail("cchadavid12@gmail.com", "dfloressi@unsa.edu.pe", message)
server.quit()

print("Correo enviado exitosamente")

#--------------------           CORREO            ------------#

