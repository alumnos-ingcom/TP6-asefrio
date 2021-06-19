################
# Agustin Anhorn - @agusanhorn
# Tomás Sautú - @TomasSautu
# Marcio Betanzo - @Marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def quitar_acentos_mayusculas_comas(texto):
    texto = texto.lower()
    texto = texto.replace(",", "")
    texto = texto.replace(" ", "")
    for j in texto:
        if j == "á":
            texto = texto.replace(j, "a")
        if j == "é":
            texto = texto.replace(j, "e")
        if j == "í":
            texto = texto.replace(j, "i")
        if j == "ó":
            texto = texto.replace(j, "o")
        if j == "ú":
            texto = texto.replace(j, "u")
    return texto

def definir_anagrama(texto1, texto2):
    texto1 = quitar_acentos_mayusculas_comas(texto1)
    texto2 = quitar_acentos_mayusculas_comas(texto2)
    if len(texto1) == len(texto2):
        try:
            for i in texto1:
                texto2.index(i)
            for z in texto2:
                texto1.index(z)
            return True
        except:
            return False
    else:
        return False

def principal():
    texto1 = "Anagrama"
    texto2 = "amar, gana"
    resultado = definir_anagrama(texto1, texto2)
    if resultado:
        print(f"{texto1} y {texto2} son anagramas entre si")
    else:
        print(f"{texto1} y {texto2} no son anagramas entre si")

if __name__ == "__main__":
    principal()
