from datetime import datetime
from Alumno import Alumno
from Curso import Curso
import smtplib
import getpass

#AULA 301 DE INGENIRIA / INGENIERIA DE SISTEMAS
#8:00  - 10:00          --->    Estructura de Datos (12 alumnos)
#10:00 - 12:00          --->    Programación Web (15 alumnos)
#14:00 - 16:00          --->    Arquitectura de Datos (10 alumnos)
#16:00 - 18:00          --->    Arquitectura de Computadoras (18 alumnos)






#--------------------           TIME            ------------#

print(datetime.now().strftime("%H:%M:%S"))
hora = datetime.now().strftime("%H:%M:%S").split(sep=":")
for hor in hora:
    print(hor)

#--------------------           TIME            ------------#


#Estructura de Datos (12 alumnos)

alumno1 = []
alumno1.append(Alumno(20202131, "David1", 24))
alumno1.append(Alumno(20202132, "David2", 18))
alumno1.append(Alumno(20202133, "David3", 20))
alumno1.append(Alumno(20202134, "David4", 22))
alumno1.append(Alumno(20202135, "David5", 24))
alumno1.append(Alumno(20202136, "David6", 18))
alumno1.append(Alumno(20202137, "David7", 20))
alumno1.append(Alumno(20202138, "David8", 22))
alumno1.append(Alumno(20202139, "David9", 24))
alumno1.append(Alumno(20202140, "David10", 18))
alumno1.append(Alumno(20202141, "David11", 20))
alumno1.append(Alumno(20202142, "David12", 22))
 
EstructuraD3 = Curso("Estructura de Datos", "08:00:00", "10:00:00", "EstructuraD3@gmail.com", alumno1)       
print(EstructuraD3)

if hora[0]==("08:00:00") & hora[0] == "10:00:00":
    for alum in alumno1:
        alum.asistencia == True
    
if hora[0] == "08:00:00":
    message = EstructuraD3
    
    #--------------------           CORREO            ------------#

    subject = "Asistencia"
    message = "Subject: {}\n\n{}".format(subject, message)

    password = getpass.getpass("ingrese contraseña: ")
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()
    server.login("cchadavid12@gmail.com", password)
    server.sendmail("cchadavid12@gmail.com", "dfloressi@unsa.edu.pe", message)
    server.quit()

    print("Correo enviado exitosamente")

    #--------------------           CORREO            ------------#

#Programación Web (15 alumnos)

alumno2 = []
alumno2.append(Alumno(20202131, "David1", 24))
alumno2.append(Alumno(20202132, "David2", 18))
alumno2.append(Alumno(20202133, "David3", 20))
alumno2.append(Alumno(20202134, "David4", 22))
alumno2.append(Alumno(20202135, "David5", 24))
alumno2.append(Alumno(20202136, "David6", 18))
alumno2.append(Alumno(20202137, "David7", 20))
alumno2.append(Alumno(20202138, "David8", 22))
alumno2.append(Alumno(20202139, "David9", 24))
alumno2.append(Alumno(20202140, "David10", 18))
alumno2.append(Alumno(20202141, "David11", 20))
alumno2.append(Alumno(20202142, "David12", 22))
alumno2.append(Alumno(20202143, "David13", 24))
alumno2.append(Alumno(20202144, "David14", 18))
alumno2.append(Alumno(20202145, "David15", 20))
 
ProgramacionW3 = Curso("Programación Web", "10:00:00", "12:00:00", "ProgramacionW3@gmail.com", alumno2)       
print(ProgramacionW3)

if hora[0]==("10:00:00") & hora[0] == "12:00:00":
    for alum in alumno1:
        alum.asistencia == True
    
if hora[0] == "10:00:00":
    message = ProgramacionW3
    
    #--------------------           CORREO            ------------#

    subject = "Asistencia"
    message = "Subject: {}\n\n{}".format(subject, message)

    password = getpass.getpass("ingrese contraseña: ")
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()
    server.login("cchadavid12@gmail.com", password)
    server.sendmail("cchadavid12@gmail.com", "dfloressi@unsa.edu.pe", message) #ProgramacionW3@gmail.com
    server.quit()

    print("Correo enviado exitosamente")

    #--------------------           CORREO            ------------#

#Arquitectura de Datos (10 alumnos)

alumno3 = []
alumno3.append(Alumno(20202131, "David1", 24))
alumno3.append(Alumno(20202132, "David2", 18))
alumno3.append(Alumno(20202133, "David3", 20))
alumno3.append(Alumno(20202134, "David4", 22))
alumno3.append(Alumno(20202135, "David5", 24))
alumno3.append(Alumno(20202136, "David6", 18))
alumno3.append(Alumno(20202137, "David7", 20))
alumno3.append(Alumno(20202138, "David8", 22))
alumno3.append(Alumno(20202139, "David9", 24))
alumno3.append(Alumno(20202140, "David10", 18))
 
ArquitecturaD4 = Curso("Arquitectura de Datos", "14:00:00", "16:00:00", "ArquitecturaD4@gmail.com", alumno3)       
print(ArquitecturaD4)

if hora[0]==("14:00:00") & hora[0] == "16:00:00":
    for alum in alumno1:
        alum.asistencia == True
    
if hora[0] == "16:00:00":
    message = ArquitecturaD4
    
    #--------------------           CORREO            ------------#

    subject = "Asistencia"
    message = "Subject: {}\n\n{}".format(subject, message)

    password = getpass.getpass("ingrese contraseña: ")
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()
    server.login("cchadavid12@gmail.com", password)
    server.sendmail("cchadavid12@gmail.com", "dfloressi@unsa.edu.pe", message) #ArquitecturaD4@gmail.com
    server.quit()

    print("Correo enviado exitosamente")

    #--------------------           CORREO            ------------#



#Arquitectura de Computadoras (18 alumnos)

alumno4 = []
alumno4.append(Alumno(20202131, "David1", 24))
alumno4.append(Alumno(20202132, "David2", 18))
alumno4.append(Alumno(20202133, "David3", 20))
alumno4.append(Alumno(20202134, "David4", 22))
alumno4.append(Alumno(20202135, "David5", 24))
alumno4.append(Alumno(20202136, "David6", 18))
alumno4.append(Alumno(20202137, "David7", 20))
alumno4.append(Alumno(20202138, "David8", 22))
alumno4.append(Alumno(20202139, "David9", 24))
alumno4.append(Alumno(20202140, "David10", 18))
alumno4.append(Alumno(20202141, "David11", 20))
alumno4.append(Alumno(20202142, "David12", 22))
alumno4.append(Alumno(20202143, "David13", 24))
alumno4.append(Alumno(20202144, "David14", 18))
alumno4.append(Alumno(20202145, "David15", 20))
alumno4.append(Alumno(20202146, "David16", 20))
alumno4.append(Alumno(20202147, "David17", 22))
alumno4.append(Alumno(20202148, "David18", 24))
 
ArquitecturaC0 = Curso("Arquitectura de Computadoras", "16:00:00", "18:00:00", "ArquitecturaC0@gmail.com", alumno4)       
print(ArquitecturaC0)

if hora[0]==("16:00:00") & hora[0] == "18:00:00":
    for alum in alumno1:
        alum.asistencia == True
    
if hora[0] == "16:00:00":
    message = ArquitecturaC0
    
    #--------------------           CORREO            ------------#

    subject = "Asistencia"
    message = "Subject: {}\n\n{}".format(subject, message)

    password = getpass.getpass("ingrese contraseña: ")
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()
    server.login("cchadavid12@gmail.com", password)
    server.sendmail("cchadavid12@gmail.com", "dfloressi@unsa.edu.pe", message) #ArquitecturaC0@gmail.com
    server.quit()

    print("Correo enviado exitosamente")

    #--------------------           CORREO            ------------#


