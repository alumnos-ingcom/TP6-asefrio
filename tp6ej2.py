################
# Agustin Anhorn - @agusanhorn
# Tomás Sautú - @TomasSautu
# Marcio Betanzo - @Marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp6ej1 import definir_anagrama


def procesar_archivo():
    archivo = open("anagramas.txt", "r", encoding = "utf-8")
    resultados = ""
    for linea in archivo:
        linea.split()
        texto_1_sin_guion = []
        texto_2_sin_guion = []
        guion = linea.index("-")
        texto_1_sin_guion.append(linea[:guion])
        texto_2_sin_guion.append(linea[guion+1:])
        texto_1 = "".join(texto_1_sin_guion)
        texto_2 = "".join(texto_2_sin_guion)
        texto_1 = texto_1.strip()
        texto_2 = texto_2.strip()
        anagrama = definir_anagrama(texto_1, texto_2)
        anagrama = str(anagrama)
        devolver_resultado = anagrama + " " + linea
        resultados += devolver_resultado
    return resultados
        

def principal():
    anagramas = procesar_archivo()
    anagramas = anagramas.replace("False", "Estos textos no son anagramas entre si -->")
    anagramas = anagramas.replace("True", "Estos textos son anagramas entre si -->")
    print(anagramas)
    
    
    
if __name__ == "__main__":
    principal()



