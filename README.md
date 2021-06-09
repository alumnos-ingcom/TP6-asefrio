# TP6-plantilla Python

Adios restricciones de funcionalidad, usen todo lo que esté disponible de Python.

## Forma de entrega
* En los ejercicios que se pide crear un archivo, agregen uno de ejemplo al repositorio.

* Cada punto debe ser entregado en un archivo independiente

* El nombre de cada archivo debe ser ser `tp6ej` seguido del numero de ejercicio mas `.py` (el primer ejercicio sera entonces `tp6ej1.py`

* Cada punto esta dividido en dos partes; la función a implementar y el programa que hace uso de la misma.

* Toda la parte interactiva con el usuario (`input`/`print`) debe estar implementadada en la función `principal()`.

* Cada archivo debe seguir la estructura indicada dentro del archivo `plantilla.py`, reemplacen con su nombre y nombre de usuario de GitHub. 

* Siguiendo con la `plantilla.py`; el programa que hace uso de lo que  debe residir dentro de la función `principal` de forma de que pueda ser ignorado al usarlo como libreria. (Al final de este documento copio la plantilla para referencia tambien)

* En ningún caso se aceptara el uso de variables globales. Toda la información necesaria para el funcionamiento de las funciones a desarrollar tienen que ser pasados como argumentos de las mismas.

* En este trabajo tampoco no se provee el prototipo de la funcion a implementar. Con un criterio similar, creen la funcion que cumpla con la consigna de manera separada a la que interactua con el usuario. Si estan muy trabados podemos conversar cual es la forma que puede tener.

* Usen nombres de variables descriptivos siempre.

* Los nombres y el formato general, deben seguir lo indicado por el PEP8.

## Importante
~~Muchas de las funciones pedidas ya se encuentran implementadas como parte de Python, implementen las funciones sin depender de esta funcionalidad integrada, sin embargo, pueden usar esta funcionalidad para verificar su funcionamiento. Esto incluye tambíen a los atajos, usen lazos.~~

## Importante

Muchos de los ejercicios son mas simples de implementar en multiples funciones separadas

### Anagrama

Implementar una funcion que determine si dos cadenas son anagramas entre si, ignorando espacios y diferencias entre mayusculas y minusculas. (En el repositorio hay un archivo con ejemplos)

#### Ejemplos:
 * Trama – Marta
 * Riesgo – Sergio
 * Cardiografía – radiografía

### Anagrama II

Procesar el archivo de anagramas y verificar si todos los de la lista son anagramas. Solo es necesario indicar las palabras de cada linea son anagramas entre si. 

Envien las palabras evaluadas y si son o no anagramas entre si por consola.

### Copiadora

Crear un programa que solicite al usuario un archivo de entrada y uno de salida para copiar el contenido de un archivo en el otro.

### Codificador

Usando la función de para codificación del cesar el TP anterior, implementar las funciones necesarias para
que se le solicite al usuario un archivo a codificar y la rotación. El archivo de salida es el mismo pero agregando al final `.cesar`

La excepcion a capturar si el archivo no existe es `FileNotFoundError`


### Descodificador

Usando la funcion para decodificar del César del TP anterior, implementar las funciones necesarias para tomar una archivo codificado (`.cesar`) y descodificarlo en un archivo nuevo que termine en `.decode` (esto es para evitar romper el archivo original).

### Etiquetas HTML

HTML, siglas en inglés de HyperText Markup Language (‘lenguaje de marcado de hipertexto’), hace referencia al lenguaje de marcado para la elaboración de páginas web.

HTML es un lenguaje de marcado que nos permite indicar la estructura de nuestro documento mediante etiquetas. Este lenguaje nos ofrece una gran adaptabilidad, una estructuración lógica y es fácil de interpre­tar tanto por humanos como por máquinas. 

Los elementos son la estructura básica de HTML. Los elementos tienen dos propiedades básicas: atributos y contenido. Cada atributo y contenido tiene ciertas restricciones para que se considere válido al documento HTML. Un elemento generalmente tiene una etiqueta de inicio (por ejemplo, `<nombre-de-elemento>`) y una etiqueta de cierre (por ejemplo, `</nombre-de-elemento>`). 

Una etiqueta puede tener atributos de valor que aportan información adicional a la etiqueta. Y para esta versión del generador de páginas no las trataremos para mantener todo lo más simple posible.

Por el momento, no nos preocupemos por limitar la etiqueta a la [lista de etiquetas](https://www.mclibre.org/consultar/htmlcss/html/html-etiquetas.html).

```python
def hace_etiqueta(contenido, etiqueta):
    '''
    Retorna el contenido envuelto en una etiqueta como está indicado en el segundo argumento.
    La funcion llamada con contenido="Hola" y etiqueta="h1" retornará
    <h1>Hola</h1>
    '''
    pass
    
def hace_comenta(contenido):
    '''
    Retorna el contenido envuelto en las marcas de comentario HTML
    <!--  -->
    (separen las marcas del contenido con un espacio)
    '''
    pass
	'''
```
La razon de que el contenido es un string; es que la funcion puede recibir lo que previamente fue 'hecho etiqueta'

```python

>>> encabezado = hace_etiqueta('Hola HTML', 'h1')
>>> print(encabezado)

>>> parrafo = hace_etiqueta(encabezado+' Párrafo', 'p')
>>> print(parrafo)
<p><h1>Hola HTML</h1>Párrafo</p>
```

Usando esa funcion en `principal()`, creen una página simple (puede quedar todo en una sola linea) con la siguiente estructura como mínimo.

```html
<html>
<body>
<h1>Hola HTML</h1>
<p>Esto es un párrafo</p>
</body>
</html>
```

Hay muchisimo más en la generación de páginas HTML, pero con esto tenemos mucho más que suficiente.
Por más que el navegador se queje, **no tomen recaudos** con las etiquetas que sean solicidatas.

#### Opcional
Envien la página generada a un archivo cuyo nombre pueda elegir el usuario.

### Etiquetas HTML parte 2 (opcional)

Los elementos en HTML tienen atributos; estos son valores adicionales que configuran los elementos o ajustan su comportamiento de diversas formas para cumplir los criterios de los usuarios. Los mismos se encuentran en la primera etiqueta y son usados para cosas como.

#### Enlaces (A de ancla)
Los enlaces hacia otras paginas se crean utilizando la etiqueta `<a>` con el atributo `href`

```html
<a href="https://www.unrn.edu.ar">Universidad Nacional de Rio Negro</a>
<!-- Ejemplo generico -->
<a href="URL del enlace">Texto del enlace</a>
```
Diccionario para el ejemplo
```python
diccionario = {"src" : "https://www.unrn.edu.ar"}
```
#### Imagenes (IMaGen)

Insertar una imágen en una página se logra utilizando el atributo `src` en el que se indica la dirección web de la imagen a mostrar.
Las paginas solo necesitan referenciar la imagen, la direccion URL de la misma puede ser relativa a la carpeta en donde está guardada en disco. En tal caso, la direccion solo necesita que el atributo src contenga el nombre del archivo: `src="foto.jpg"`
```html
<img src="https://www.unrn.edu.ar/images/favicon/apple-touch-icon-152x152.png">Logo UNRN en internet</img>
<img src="foto.jpg">Imagen local</img>
<!-- Ejemplo generico -->
<img src="URL de la imágen">Texto alternativo</img>
```
```python
diccionario = {"src" : "https://www.unrn.edu.ar/images/favicon/apple-touch-icon-152x152.png"}
```

#### Combinaciones

Es posible crear una imagen con que actue como enlace combinando la etiqueta `A` con un `IMG` dentro

```html
<a href="https://www.unrn.edu.ar"><img src="https://www.unrn.edu.ar/images/favicon/apple-touch-icon-152x152.png">Logo UNRN en internet</img></a>
```

#### Consigna

Agregar un argumento adicional a la función que crea etiquetas, de forma que acepte un diccionario para agregar los atributos a la etiqueta y crear un programa que cree un sitio simple por medio de las funciones y lo guarde como `pagina.html`

Por más que el navegador se queje, **no tomen recaudos** con los atributos que le agreguen a las etiquetas.