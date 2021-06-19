################
# Agustin Anhorn - @agusanhorn
# Tomás Sautú - @TomasSautu
# Marcio Betanzo - @Marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def hacer_etiquetas(contenido, etiqueta):
    
    etiqueta_contenido = f"<{etiqueta}>{contenido}</{etiqueta}>"
    
    return etiqueta_contenido


def principal():
    
    etiqueta_mensaje_principal = hacer_etiquetas("Hola HTML", "h1")
    etiqueta_parrafo = hacer_etiquetas("Esto es un párrafo", "p")    
    etiqueta_body = hacer_etiquetas(etiqueta_mensaje_principal + etiqueta_parrafo, "body")
    etiqueta_html = hacer_etiquetas(etiqueta_body, "html")
    print(etiqueta_html)

if __name__ == "__main__":
    principal()