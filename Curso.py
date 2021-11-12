from Alumno import Alumno


from datetime import datetime
import time

class Curso:
        
    def __init__(self, curso, timeInit, timeFinish, correo):
        self.curso = curso
        self.timeInit = timeInit
        self.timeFinish = timeFinish
        self.teacher = correo
        
        alumno = []
        alumno.append(Alumno(20202136, "David6", 24))
        alumno.append(Alumno(20202133, "David3", 18))
        alumno.append(Alumno(20202134, "David4", 20))
        alumno.append(Alumno(20202135, "David5", 22))
        self.alumnos = alumno
        
    def __str__(self):
        mostrar = "CURSO:\t"+self.curso+"\n"
        horario = "INICIA: "+self.timeInit+"\nACABA: "+self.timeFinish+"\n"
        docente = "DOCENTE:\t"+self.teacher+"\n\n"
        nombres = "ALUMNOS DEL CURSO\n"
        alumnos = ""
        for a in self.alumnos:
            alumnos = alumnos + str(a) + "\n"
            
        return mostrar + horario + docente + nombres + alumnos 
        
    
   
#print(datetime.now().strftime("%H:%M:%S"))
#hora = datetime.now().strftime("%H:%M:%S").split(sep=":")
#for hor in hora:
#    print(hor)


        
d = Curso("matematica", "11:30:00", "11:50:00", "teacher12@gmail.com")
print(d)

