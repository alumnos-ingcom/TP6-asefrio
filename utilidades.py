################
# Agustin Anhorn - @agusanhorn
# Tomás Sautú - @TomasSautu
# Marcio Betanzo - @Marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

class ArchivoInexistente(Exception):
    """Esta es la excepción para el manejo de archivos inexistentes"""
    pass

def ingreso_entero(mensaje):
    """
    Esta funcion convierte un número en texto en un número entero.
    """
    ingreso = input(mensaje)
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número genio!") from err
    return entero

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
    
def obtener_distancia(numero_uno, numero_dos):
    if (numero_uno == numero_dos):
        return 0
    contador = 0
    if (numero_uno < numero_dos):
        while numero_uno < numero_dos:
            contador = contador + 1
            numero_uno = numero_uno + 1
        return contador
    if (numero_uno > numero_dos):
        while numero_uno > numero_dos:
            contador = contador + 1
            numero_dos = numero_dos + 1
        return contador
    
def borrar_extensiones(nombre):
    nombre_sin_extension = list()
    for letra in nombre:
        if (letra == "."):
            nuevo_nombre = "".join(nombre_sin_extension)
            return nuevo_nombre
        else:
            nombre_sin_extension.append(letra)

def crear_archivo_vacio(nombre):
    archivo_encriptado = open(nombre, "w+")
    archivo_encriptado.close()
    
def obtener_extension(nombre):
    nombre = nombre[::-1]
    extension = borrar_extensiones(nombre)
    extension = extension[::-1]
    return extension



# def principal():
#     """Toda la interacción con el usuario va acá"""
#     
#     print(encriptar_cesar("abcde", 1))
#     
#     pass
# 
# if __name__ == "__main__":
#     principal()

