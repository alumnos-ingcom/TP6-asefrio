################
# Tomás Sautú - @TomasSautu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_entero, IngresoIncorrecto

def cifrado_cesar(rotacion, texto, signo = 1):
    texto_encriptado_lista = []
    for i in texto:
        dato_texto = ord(i) #Se convierten los caracteres a su valor unicode
        
        #MAYÚSCULAS
        if dato_texto >= ord('A') and dato_texto <= ord('Z'):  #Se comprueba si el carácter es una Mayúscula
            dato_texto_mayuscula = dato_texto + (rotacion * signo) #En este punto se le aplica la rotación necesaria (dependiendo de si estamos encriptando o desenciptando, cambio que se realiza con el "signo"
            if dato_texto_mayuscula > ord('Z'):        #Se comprueba si el carácter ya encriptado pasa al limite derecho de las Mayúsculas ("Z")
                while dato_texto_mayuscula > ord('Z'): #Se le resta hasta que este dentro de las letras Mayúsculas
                    dato_texto_mayuscula -= 26
                dato_texto = chr(dato_texto_mayuscula)
            elif dato_texto_mayuscula < ord('A'):     #Se comprueba si el carácter ya encriptado pasa al limite izquierdo de las Mayúsculas ("A")
                while dato_texto_mayuscula < ord('A'):#Se le suma hasta que este dentro de las letras Mayúsculas
                    dato_texto_mayuscula += 26
                dato_texto = chr(dato_texto_mayuscula)
            else:
                dato_texto = chr(dato_texto_mayuscula) #Si el carácter ya estaba dentro del parametro no se modifica
             
        #MINÚSCULAS
        elif dato_texto >= ord('a') and dato_texto <= ord('z'): #Se comprueba si el carácter es Minúscula
            dato_texto_minuscula = dato_texto + (rotacion * signo) #Se hace la rotación devida
            if dato_texto_minuscula > ord('z'):        #Se comprueba si el carácter ya encriptado pasa al limite derecho de las Minúsculas ("z")
                while dato_texto_minuscula > ord('z'): #Se le resta hasta que este dentro de las letras Minúsculas
                    dato_texto_minuscula -= 26
                dato_texto = chr(dato_texto_minuscula)
            elif dato_texto_minuscula < ord('a'):      #Se comprueba si el carácter ya encriptado pasa al limite izquierdo de las Minúsculas("a")
                while dato_texto_minuscula < ord('a'): #Se le resta hasta que este dentro de las letras Minúsculas
                    dato_texto_minuscula += 26
                dato_texto = chr(dato_texto_minuscula)
            else:
                dato_texto = chr(dato_texto_minuscula) #Si el carácter ya estaba dentro del parametro no se modifica
                
        #NÚMEROS
        elif dato_texto >= ord('0') and dato_texto <= ord('9'): #Se comprueba si el carácter es un número
            dato_texto_numero = dato_texto + (rotacion * signo) #Se hace la rotación
            if dato_texto_numero > ord('9'):                    #Se comprueba si el carácter ya encriptado pasa al limite derecho de los números ("9")
                while dato_texto_numero > ord('9'):             #Se le resta hasta que este dentro de los números
                    dato_texto_numero -= 10
                dato_texto = chr(dato_texto_numero)
            elif dato_texto_numero < ord('0'):                  #Se comprueba si el carácter ya encriptado pasa al limite izquierdo de los números ("0")
                while dato_texto_numero < ord('0'):             #Se le suma hasta que este dentro de los números
                    dato_texto_numero += 10
                dato_texto = chr(dato_texto_numero)
            else:
                dato_texto = chr(dato_texto_numero)             #Si el carácter ya estaba dentro del parametro no se modifica
        else:
            dato_texto = chr(dato_texto)                        #Si los caracteres no son a-z, A-Z ó 0-9 se los devuelve como estaban
        texto_encriptado_lista.append(dato_texto)
    texto_encriptado = "".join(texto_encriptado_lista)          #Se convierte la lista de los carácteres en un texto completo
    return texto_encriptado                                     #Se devuelve el texto

def prueba():
    #Esta parte sirve para saber si se va a ENCRIPTAR o DESENCRIPTAR
    utilidad = True
    utilidad = ingreso_entero("""Este programa le permitirá hacer una encriptación o desencriptacion cesar con la rotación y mensaje que usted ingrese
Desea Encriptar o Desencriptar?

Encriptar = 1
Desencriptar = 2

""")
    if utilidad == 1:
        utilidad = True
    elif utilidad == 2:
        utilidad = False
    else:
        raise IngresoIncorrecto("No era una opcion") #Excepción si no son ninguno de los valores para utilidad
        
    if utilidad:
        print("""Este programa hará una ENCRIPTACIÓN con Cifrado Cesar con la rotación y mensaje que usted ingrese
    (¡tener en cuentan que las tildes darán un error de encriptación!)""")
        rotacion = ingreso_entero("Ingrese la rotación con la que quiere encriptar: ")
        texto = input("Ingrese el texto que quiere encriptar: ")
        encriptado = codificar_cifrado_cesar(rotacion, texto, signo = 1) #FIJARSE QUE EL ARGUMENTO "signo" ESTÁ CON "= 1", DE ESTA FORMA ENCRIPTA        print(f'El texto encripatado con una rotación de {rotacion} es: "{encriptado}"')
    else:
        print("""Este programa hará una DESENCRIPTACIÓN con Cifrado Cesar con la rotación y mensaje que usted ingrese
    (¡tener en cuenta que las tildes darán un error de encriptación!)""")
        rotacion = ingreso_entero("Ingrese la rotación con la que se encriptó: ")
        texto = input("Ingrese el texto encriptado: ")
        encriptado = codificar_cifrado_cesar(rotacion, texto, signo = -1) #FIJARSE QUE EL ARGUMENTO "signo" ESTÁ CON "= -1", DE ESTA FORMA DESENCRIPTA
        print(f'El texto encripatado {texto} desencriptado con una rotación de {rotacion} es: "{encriptado}"')

if __name__ == "__main__":
    prueba()