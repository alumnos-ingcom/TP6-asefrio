################
# Agustin Anhorn - @agusanhorn
# Tomás Sautú - @TomasSautu
# Marcio Betanzo - @Marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def copiar_archivos(nombre_archivo, nombre_copia):
    archivo = open(nombre_archivo,'r')
    copia_archivo = open(nombre_copia,'w')
    for line in archivo:
        copia_archivo.write(line)
        
    archivo.close()
    copia_archivo.close()

def principal():
    nombre_archivo = input("Ingrese el nombre el archivo que quiere copiar: ")
    nombre_copia = input("Ingrese el nombre del archivo en el que quiere copiar: ")
    copiar_archivos(nombre_archivo, nombre_copia)
    print("El archivo fue copiado con exito!")

if __name__ == "__main__":
    principal()
