from utilidades import ingreso_entero, IngresoIncorrecto

def cifrado_cesar(rotacion, texto, utilidad = 1):
    encriptar = [ord('a'), ord('A'), ord('z'), ord('0')]
    desencriptar = [ord('Z'), ord('9'), ord('z'), ord('0')]
    texto_encriptado_lista = []
    rotacion *= utilidad
    if utilidad == 1:
        salto = encriptar
    else:
        salto = desencriptar
    for i in texto:
        dato_texto = ord(i)
        if (dato_texto >= ord('A') and dato_texto <= ord('Z')) or (dato_texto >= ord('a') and dato_texto <= ord('z')) or (dato_texto >= ord('0') and dato_texto <= ord('9')) :
            for _ in range(0, rotacion, utilidad):
                dato_texto += utilidad
                #Comprueba si el carácter esta entre los carácteres especiales de la "Z" a la "a". Si es asi, salta hacia la "a" ó "Z"
                if dato_texto > ord('Z') and dato_texto < ord('a'):
                    dato_texto = salto[0]
                #Comprueba si el carácter esta entre los carácteres especiales del "9" a la "A". Si es asi, salta hacia la "A" ó "9"
                if dato_texto > ord('9') and dato_texto < ord('A'):
                    dato_texto = salto[1]
                #Comprueba si el carácter esta entre los carácteres especiales antes del "0". Si es asi, salta hacia la "z" ó "0"
                if dato_texto < ord('0'):
                    dato_texto = salto[2]
                #Comprueba si el carácter esta entre los carácteres especiales despues de la "z". Si es asi, salta hacia la "0" ó "z"
                if dato_texto > ord('z'):
                    dato_texto = salto[3]

            dato_texto = chr(dato_texto)
        else:
            dato_texto = chr(dato_texto)
        texto_encriptado_lista.append(dato_texto)  
    texto_encriptado = "".join(texto_encriptado_lista)
    return texto_encriptado

def principal():
    utilidad = True
    utilidad = ingreso_entero("""Este programa le permitirá hacer una encriptación o desencriptacion cesar con la rotación y mensaje que usted ingrese
Usted quiere Encriptar o Desencriptar?
Encriptar = 1
Desencriptar = 2
""")
    if utilidad == 1:
        utilidad = True
    elif utilidad == 2:
        utilidad = False
    else:
        raise IngresoIncorrecto("No era una opcion")
        
    if utilidad:
        print("""Este programa hará una ENCRIPTACIÓN con Cifrado Cesar con la rotación (siempre número positivo) y mensaje que usted ingrese
    (¡tener en cuentan que las tildes darán un error de encriptación!)""")
        rotacion = ingreso_entero("Ingrese la rotación con la que quiere encriptar: ")
        if rotacion > 0:
            texto = input("Ingrese el texto que quiere encriptar: ")
            encriptado = cifrado_cesar(rotacion, texto)
            print(f'El texto encripatado con una rotación de {rotacion} es: "{encriptado}"')
        else:
            raise IngresoIncorrecto("Tiene que ser un número positivo")
    else:
        print("""Este programa hará una DESENCRIPTACIÓN con Cifrado Cesar con la rotación y mensaje que se usaron para encriptar
    (¡tener en cuenta que las tildes darán un error de encriptación!)""")
        rotacion = ingreso_entero("Ingrese la rotación con la que se encriptó: ")
        texto = input("Ingrese el texto encriptado: ")
        encriptado = cifrado_cesar(rotacion, texto, utilidad = -1 )
        print(f'El texto encripatado {texto} desencriptado con una rotación de {rotacion} es: "{encriptado}"')

if __name__ == "__main__":
    principal()