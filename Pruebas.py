import smtplib
import getpass


message = "Hola mundo de gmail"
subject = "Pyhton"
message = "Subject: {}\n\n{}".format(subject, message)

password = getpass.getpass("ingrese contraseña: ")
server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()
server.login("cchadavid12@gmail.com", password)
server.sendmail("cchadavid12@gmail.com", "dfloressi@unsa.edu.pe", message)
server.quit()

print("Correo enviado exitosamente")

