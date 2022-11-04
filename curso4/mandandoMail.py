import smtplib
import time
import data
veces = 0

server = smtplib.SMTP('smtp.gmail.com', 587) #primero ponemos el mail(gmail en mi caso) depsues el puerto 587
server.starttls()
server.login(data.mail, data.contraseña)
while True:

    server.sendmail(data.remitente, data.lector, data.message) # 1.remitente 2.lector 3. mensaje
    veces += 1
    print("Ya se enviaron: ", veces, "mails")
    #time.sleep(10)

server.quit()
