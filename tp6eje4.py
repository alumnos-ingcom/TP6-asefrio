################
# Agustin Anhorn - @agusanhorn
# Tomás Sautú - @TomasSautu
# Marcio Betanzo - @Marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_entero, IngresoIncorrecto, ArchivoInexistente, cifrado_cesar, borrar_extensiones, crear_archivo_vacio

def encriptar_archivo(n_archivo, rotacion):

    
    #Intentamos abrir el archivo
    try:
        archivo = open(n_archivo)
    except FileNotFoundError as err:
        #Si no existe le mandamos la excepción
        raise ArchivoInexistente("El archivo no existe!") from err
    
    #Creamos una lista con cada línea
    texto = archivo.readlines()
    #Creamos una lista vacía que será llenada con las líneas encriptadas
    texto_encriptado = list()
    
    
    
    #Un for leyendo línea por línea
    for linea in texto:
        
        #Encriptamos una nueva línea en cada vuelta
        linea_encriptada = cifrado_cesar(rotacion, linea, 1)
        #Metemos la encriptación en la lista
        texto_encriptado.append(linea_encriptada)
    
    #Cerramos el archivo
    archivo.close()
    
    nombre_archivo = borrar_extensiones(n_archivo)
    nombre_archivo = nombre_archivo + ".cesar"
    
    crear_archivo_vacio(nombre_archivo)
    archivo_encriptacion = open(nombre_archivo, "a")
    
    for linea in texto_encriptado:
        archivo_encriptacion.write(linea)
    
    archivo_encriptacion.close()
    
    pass


def principal():
    
    print("Ingrese el nombre del archivo que desea encriptar: ")
    print("Recuerde que el archivo debe existir en la misma ruta donde ejecuta")
    print("este programa y que tiene que agregar la extensión del mismo.")
    archivo = input("> : ")
    rotacion = ingreso_entero("Ingrese la rotación para encriptar: # ")
    
    if (rotacion <= 0):
        raise IngresoIncorrecto("El número debe ser mayor a 0!")
    
    
    encriptar_archivo(archivo, rotacion)
    
    pass

if __name__ == "__main__":
    principal()


