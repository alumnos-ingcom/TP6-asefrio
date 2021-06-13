def es_numero(dato):
    if (dato > 47 and dato < 58):
        return True
    else:
        return False
def es_letra_mayus(dato):
    if (dato > 64 and dato < 91):
        return True
    else:
        return False
def es_letra_minus(dato):
    if (dato > 96 and dato < 123):
        return True
    else:
        return False


def encriptar_cesar(texto, rotacion, signo = 1):
    
    lista_nuevo_texto = []
    
    carac_mayus_z = ord("Z")
    carac_minus_z = ord("z")
    carac_cero = ord("0")
    carac_nueve = ord("9")
    
    for i in texto:
        dato_unicode = ord(i)
        dato_encript = dato_unicode + (rotacion * signo)
        
        ## Si el valor de entrada es un número, letra mayúscula o minúscula:
        if (es_letra_mayus(dato_unicode) or
            es_letra_minus(dato_unicode) or
            es_numero(dato_unicode)):
            
            ## Si el valor de entrada es un número, tomamos todos los caminos posibles
            if (es_numero(dato_unicode)):
                
                ## Si el dato encriptado es mayor a "9",
                ## le sumamos 7 (carácteres entre números y mayúsculas)
                if (dato_encript > carac_nueve):
                    dato_encript = dato_encript + 7
                    
                ## Si el dato encriptado es mayor a "Z",
                ## le sumamos 6 (carácteres entre mayúsculas y minúsculas)
                if (dato_encript > carac_mayus_z):
                    dato_encript = dato_encript + 6
                    
                ## Si el dato encriptado es mayor a "z",
                ## obtenemos la distancia entre "z" y el dato encriptado
                ## y se la sumamos al carácter anterior a "0"
                if (dato_encript > carac_minus_z):
                    dist = obtener_distancia(dato_encript, carac_minus_z)
                    dato_encript = carac_cero - 1 + dist
                    
            ## Si el valor de entrada es letra mayúscula, tomamos todos los caminos posibles 
            if (es_letra_mayus(dato_unicode)):
                
                ## Si el dato encriptado es mayor a "Z",
                ## le sumamos 6 (carácteres entre mayúsculas y minúsculas)
                if (dato_encript > carac_mayus_z):
                    dato_encript = dato_encript + 6
                    
                ## Si el dato encriptado es mayor a "z",
                ## obtenemos la distancia entre "z" y el dato encriptado
                ## y se la sumamos al carácter anterior a "0"
                if (dato_encript > carac_minus_z):
                    dist = obtener_distancia(dato_encript, carac_minus_z)
                    dato_encript = carac_cero - 1 + dist
                    
                    ## Si el dato encriptado es mayor a "9",
                    ## le sumamos 7 (carácteres entre números y mayúsculas)
                    if (dato_encript > carac_nueve):
                        dato_encript = dato_encript + 7
                        
            ## Si el valor de entrada es letra minúscula, tomamos todos los caminos posibles
            if (es_letra_minus(dato_unicode)):
                
                ## Si el dato encriptado es mayor a "z",
                ## obtenemos la distancia entre "z" y el dato encriptado
                ## y se la sumamos al carácter anterior a "0"
                if (dato_encript > carac_minus_z):
                    dist = obtener_distancia(dato_encript, carac_minus_z)
                    dato_encript = carac_cero - 1 + dist
                    
                    ## Si el dato encriptado es mayor a "9",
                    ## le sumamos 7 (carácteres entre números y mayúsculas)
                    if (dato_encript > carac_nueve):
                        dato_encript = dato_encript + 7
                        
                    ## Si el dato encriptado es mayor a "Z",
                    ## le sumamos 6 (carácteres entre mayúsculas y minúsculas)
                    if (dato_encript > carac_mayus_z):
                        dato_encript = dato_encript + 6
                    
            lista_nuevo_texto.append(chr(dato_encript))
            
        ## Si no es un número, letra mayúscula o minúscula, lo dejamos pasar
        else:
            lista_nuevo_texto.append(chr(dato_unicode))
                
    nuevo_texto = "".join(lista_nuevo_texto)
    return nuevo_texto

def principal():
    #encriptar
    
    rotacion = int(input("ingrese rotación para encriptar: "))
    texto = input("texto a encriptar: ")
    texto_encriptado = encriptar_cesar(texto, rotacion)
    print(texto_encriptado)
    
    #desencriptar
    
    rotacion = int(input("ingrese rotación que se usó: "))
    texto = input("texto ya encriptado: ")
    texto_encriptado = encriptar_cesar(texto, rotacion, signo = -1) #agregar el cambio de signo (-1) en el argumento para desencriptar
    print(texto_encriptado)

if __name__ == "__main__":
     principal()