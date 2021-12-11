class Alumno:   
    
    def __init__(self, cui, name, age):
        self.cui = int(cui)
        self.name = name
        self.age = int(age)
        self.asistencia = False
        self.video = "img y videos/"+name+".mp4"
        
    def __str__(self):
        #return "CUI: " + str(self.cui) + "\nNAME: " + self.name + "\nAGE: " + str(self.age) + "\nASISTENCIA: " + str(self.asistencia) + "\nVIDEO: [" + self.video + "]\n"+"\n"
        return "CUI: " + str(self.cui) + "\nNAME: " + self.name + "\nAGE: " + str(self.age) + "\nVIDEO: [" + self.video + "]\n"+"\n"

    
    
a = Alumno(20202132, "David", 18)
b = Alumno(20202133, "Nicolas", 20)

#print(a)
   

