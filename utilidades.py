################
# Agustin Anhorn - @agusanhorn
# Tomás Sautú - @TomasSautu
# Marcio Betanzo - @Marsiocons
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def ingreso_entero(mensaje):
    """
    Esta funcion convierte un número en texto en un número entero.
    """
    ingreso = input(mensaje)
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número genio!") from err
    return entero

def encriptar_cesar(texto, rotacion):
    
    lista_nuevo_texto = []
    
    carac_mayus_z = ord("Z")
    carac_minus_z = ord("z")
    carac_cero = ord("0")
    carac_nueve = ord("9")
    
    for i in texto:
        dato_unicode = ord(i)
        dato_encript = dato_unicode + rotacion
        
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

def desencriptar_cesar(texto, rotacion):
    
    lista_nuevo_texto = []
    
    carac_mayus_a = ord("A")
    carac_minus_a = ord("a")
    carac_cero = ord("0")
    carac_minus_z = ord("z")
    
    for i in texto:
        
        dato_unicode = ord(i)
        dato_encript = dato_unicode - rotacion
        
        ## Si el valor de entrada es un número, letra mayúscula o minúscula:
        if (es_letra_mayus(dato_unicode) or
            es_letra_minus(dato_unicode) or
            es_numero(dato_unicode)):
            
            ## Si el valor de entrada es letra minúscula, tomamos todos los caminos posibles
            if (es_letra_minus(dato_unicode)):
                
                ## Si el dato encriptado es menor a "a",
                ## le restamos 6 (carácteres entre mayúsculas y minúsculas)
                if (dato_encript < carac_minus_a):
                    dato_encript =  dato_encript - 6
                    
                ## Si el dato encriptado es menor a "A",
                ## le restamos 7 (carácteres entre números y mayúsculas)
                if (dato_encript < carac_mayus_a):
                    dato_encript = dato_encript - 7
                    
                ## Si el dato encriptado es menor a "0",
                ## obtenemos la distancia del dato encriptado y "0"
                ## y se la restamos al carácter siguiente a "z"
                if (dato_encript < carac_cero):
                    dist = obtener_distancia(dato_encript, carac_cero)
                    dato_encript = carac_minus_z + 1 - dist
                    
            ## Si el valor de entrada es letra mayúscula, tomamos todos los caminos posibles 
            if (es_letra_mayus(dato_unicode)):
                
                ## Si el dato encriptado es menor a "A",
                ## le restamos 7 (carácteres entre números y letras mayúsculas)
                if (dato_encript < carac_mayus_a):
                    dato_encript = dato_encript - 7
                    
                ## Si el dato encriptado es menor a 0,
                ## obtenemos la distancia del dato encriptado y "0"
                ## y se la restamos al carácter siguiente a "z"
                if (dato_encript < carac_cero):
                    dist = obtener_distancia(dato_encript, carac_cero)
                    dato_encript = carac_minus_z + 1 - dist
                    
                    ## Si el dato encriptado es menor a "a"
                    ## le restamos 6 (carácteres entre mayúsculas y minúsculas)
                    if (dato_encript < carac_minus_a):
                        dato_encript = dato_encript - 6
                        
            ## Si el valor de entrada es un número, tomamos todos los caminos posibles
            if (es_numero(dato_unicode)):
                
                ## Si el dato encriptado es menor a "0"
                ## obtenemos la distancia del dato encriptado y "0"
                ## y se la restamos al carácter siguiente a "z"
                if (dato_encript < carac_cero):
                    dist = obtener_distancia(dato_encript, carac_cero)
                    dato_encript = carac_minus_z + 1 - dist
                    
                    ## Si el dato encriptado es menor a "a"
                    ## le restamos 6 (carácteres entre mayúsculas y minúsculas)
                    if (dato_encript < carac_minus_a):
                        dato_encript = dato_encript - 6
                        
                    ## Si el dato encriptado es menor a "A",
                    ## le restamos 7 (carácteres entre números y letras mayúsculas)
                    if (dato_encript < carac_mayus_a):
                        dato_encript = dato_encript -7
            
            lista_nuevo_texto.append(chr(dato_encript))
        
        ## Si no es un número, letra mayúscula o minúscula, lo dejamos pasar
        else:
            lista_nuevo_texto.append(chr(dato_unicode))
            
    nuevo_texto = "".join(lista_nuevo_texto)
    return nuevo_texto

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
    
def obtener_distancia(numero_uno, numero_dos):
    if (numero_uno == numero_dos):
        return 0
    contador = 0
    if (numero_uno < numero_dos):
        while numero_uno < numero_dos:
            contador = contador + 1
            numero_uno = numero_uno + 1
        return contador
    if (numero_uno > numero_dos):
        while numero_uno > numero_dos:
            contador = contador + 1
            numero_dos = numero_dos + 1
        return contador



# def principal():
#     """Toda la interacción con el usuario va acá"""
#     
#     print(encriptar_cesar("abcde", 1))
#     
#     pass
# 
# if __name__ == "__main__":
#     principal()

