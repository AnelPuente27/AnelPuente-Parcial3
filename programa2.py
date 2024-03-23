import pywhatkit

try:
#    pywhatkit.sendwhatmsg_instantly("+52 1 444 598 9769" , "Hola desde python")
    pywhatkit.sendwhatmsg_to_group("HMSd7sLfFPy4ivP0YtAqvE", " Ahora si pude", 19, 5)
    print("Mensaje enviado")
except:
    print("Error")