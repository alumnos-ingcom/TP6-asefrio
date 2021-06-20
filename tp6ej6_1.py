################
# Agustin Anhorn - @agusanhorn
# Tomás Sautú - @TomasSautu
# Marcio Betanzo - @Marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_entero

def hacer_etiquetas(contenido, etiqueta):
    
    etiqueta_contenido = f"<{etiqueta}>{contenido}</{etiqueta}>"
    
    return etiqueta_contenido

def hacer_archivo_html(contenido, nombre_archivo): 
    
    archivo_html = open(nombre_archivo + ".html", "w")
    
    archivo_html.write(contenido)
    
    archivo_html.close

def principal():
    imagen = '<img src="https://pbs.twimg.com/profile_images/1258937747064094724/yGluEShZ_400x400.jpg"/>'
    etiqueta_mensaje_principal = hacer_etiquetas("Hola HTML ^_^", "h1")
    etiqueta_parrafo = hacer_etiquetas("Esto es un párrafo", "p")
    etiqueta_body = hacer_etiquetas(etiqueta_mensaje_principal + etiqueta_parrafo + imagen, "body")
    etiqueta_html = hacer_etiquetas(etiqueta_body, "html") 
    #opcional
    opcion = ingreso_entero("""¿Desea crear el archivo con el contenido html? (0 / 1):
    Si = 0
    No = 1
    
    #""")
     
    if opcion == 0:
        nombre_archivo = input("Ingrese el nombre del archivo a crear: #")
        hacer_archivo_html(etiqueta_html, nombre_archivo)
        print("Archivo creado con éxito!.")
    else:
        print("Finalización del programa.")


if __name__ == "__main__":
    principal()


