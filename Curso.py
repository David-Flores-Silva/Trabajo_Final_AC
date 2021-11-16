class Curso:
        
    def __init__(self, curso, timeInit, timeFinish, correo, alumno = []):
        self.curso = curso
        self.timeInit = timeInit
        self.timeFinish = timeFinish
        self.teacher = correo
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
        
    
   

