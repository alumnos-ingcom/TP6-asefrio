################
# Agustin Anhorn - @agusanhorn
# Tomás Sautú - @TomasSautu
# Marcio Betanzo - @Marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#from utilidades import ingreso_entero, IngresoIncorrecto

def encriptar_archivo(n_archivo, rotacion):
    
    archivo = open(n_archivo)
    
    texto = archivo.readlines()
    
    for posicion, linea in enumerate(texto):
        
        print(f"({posicion}) > {linea}")
        
    archivo.close()
    
    pass


def principal():
    
    #archivo = input("Ingrese el nombre del archivo que desea encriptar: ")
    #rotacion = ingreso_entero("Ingrese la rotación para encriptar: # ")
    
    #encriptar_archivo(archivo, rotacion)
    
    encriptar_archivo("anagramas.txt", 1)
    
    pass

if __name__ == "__main__":
    principal()


