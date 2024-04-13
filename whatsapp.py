import pywhatkit

try:

    pywhatkit.sendwhatmsg_instantly("+524448288325", "Hola desde python" , 18,43)
    print("Mensaje enviado")
except:
    print("Error")