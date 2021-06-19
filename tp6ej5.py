################
# Agustin Anhorn - @agusanhorn
# Tomás Sautú - @TomasSautu
# Marcio Betanzo - @Marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_entero, IngresoIncorrecto, ArchivoInexistente, cifrado_cesar, borrar_extensiones, crear_archivo_vacio, obtener_extension


def desencriptar_archivo(n_archivo, rotacion):
    
    try:
        archivo = open(n_archivo)
    except FileNotFoundError as err:
        raise ArchivoInexistente("El archivo no existe!") from err
    
    extension = obtener_extension(n_archivo)
    if (extension != "cesar"):
        raise IngresoIncorrecto("El archivo no tiene extensión de encriptado!")
    
    #Creamos una lista con cada línea
    texto_encriptado = archivo.readlines()
    #Creamos una lista vacía que será llenada con las líneas desencriptadas
    texto = list()
    
    #Un for leyendo línea por línea
    for linea in texto_encriptado:
        
        #Encriptamos una nueva línea en cada vuelta
        linea_desencriptada = cifrado_cesar(rotacion, linea, -1)
        #Metemos la encriptación en la lista
        texto.append(linea_desencriptada)
    
    #Cerramos el archivo
    archivo.close()
    
    nombre_archivo = borrar_extensiones(n_archivo)
    nombre_archivo = nombre_archivo + ".decode"
    
    crear_archivo_vacio(nombre_archivo)
    archivo_desencriptado = open(nombre_archivo, "a")
    
    for linea in texto:
        archivo_desencriptado.write(linea)
    
    archivo_desencriptado.close()


def principal():
    
    print("""
    Ingrese el nombre del archivo que desea desencriptar:
    Recuerde que el archivo debe existir en la misma ruta donde ejecuta
    este programa y que tiene que agregar la extensión del mismo.
    Si la extensión no es 'cesar' el programa no funcionará.
    """)
    archivo = input("> : ")
    rotacion = ingreso_entero("Ingrese la rotación para encriptar: # ")
    
    if (rotacion <= 0):
        raise IngresoIncorrecto("El número debe ser mayor a 0!")
    
    
    desencriptar_archivo(archivo, rotacion)
    
    pass

if __name__ == "__main__":
    principal()


