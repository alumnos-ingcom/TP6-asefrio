################
# Agustin Anhorn - @agusanhorn
# Tomás Sautú - @TomasSautu
# Marcio Betanzo - @Marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp6ej1 import definir_anagrama, quitar_acentos_mayusculas_comas


def procesar_archivo():
    archivo = open("anagramas.txt", "r", encoding = "utf-8")
    lista = []
    for i in archivo:
        i.split()
        texto1 = []
        texto2 = []
        a = i.index("-")
        texto1.append(i[:a])
        texto2.append(i[a+1:])
        texto_1 = "".join(texto1)
        texto_2 = "".join(texto2)
        r = definir_anagrama(texto_1, texto_2)
        if r == True:
            lista.append(r)
        else:
            lista.append(r)
    return lista

def principal():
    anagramas = procesar_archivo()
    print(anagramas)
    
if __name__ == "__main__":
    principal()



