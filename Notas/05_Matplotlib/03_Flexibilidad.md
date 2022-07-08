# 7.4 Cuestiones de diseño

En esta breve sección, volvemos a discutir algunas decisiones de diseño que tomamos antes.


### Archivos versus iterables

Compará estos dos programas que resultan en la misma salida.

```python
# Necesita el nombre de un archivo
def read_data(nombre_archivo):
    records = []
    with open(nombre_archivo) as f:
        for line in f:
            ...
            records.append(r)
    return records

d = read_data('file.csv')
```

```python
# Necesita líneas de texto
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)
```

* ¿Cuál de las funciones `read_data()` preferís y por qué?
* ¿Cuál de las funciones permite mayor flexibilidad?

### Una idea profunda: "Duck Typing" (Identificación de patos)

[Duck Typing](https://en.wikipedia.org/wiki/Duck_typing) del inglés o en español ["Test del pato"](https://es.wikipedia.org/wiki/Duck_typing) es un concepto usado en programación para determinar si un objeto puede ser usado para un propósito en particular. Se trata de una aplicación particular del [test del pato](https://en.wikipedia.org/wiki/Duck_test) que puede resumirse así:

> Si algo se parece a un pato, nada como un pato, y hace el mismo ruido que un pato, entonces probablemente se trate de un pato.

Mientras que la primera versión de `read_data()` requiere específicamente líneas de un archivo de texto, la segunda versión funciona con *cualquier* iterable. 

```python
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records
```

Esto implica que la podemos usar con otro tipo de *líneas*, no necesariamente archivos. Veamos algunos ejemplos.


```python
# Un archivo .csv
lines = open('data.csv')
data = read_data(lines)

# Un archivo zipeado 
lines = gzip.open('data.csv.gz','rt')
data = read_data(lines)

# La entrada estándar (Standard Input), por teclado
lines = sys.stdin
data = read_data(lines)

# Una lista de cadenas
lines = ['Quinoto,50,91.1','Naranja,75,123.45', ... ]
data = read_data(lines)
```

Esto nos lleva nuevamente a la identificación de patos: es suficiente con saber que grazna como pato, camina como pato y vuela como pato para saber que podés usarlo como pato. Volveremos a esta idea al hablar de diseño de objetos, dentro de un par de clases. En este caso en particular, todos nuestros "patos" ...

```python
lines = open('data.csv')
lines = gzip.open('data.csv.gz','rt')
lines = sys.stdin
lines = ['Quinoto,50,91.1','Naranja,75,123.45', ... ]
```

son iterables de texto, por lo tanto los usaremos como "patos" en la función `read_data()`.

Si el concepto te resulta oscuro, tal vez [esta explicación](https://youtu.be/pxzLSMqU_7U) te ayude. La flexibilidad que este diseño permite es considerable. *Pregunta: ¿Debemos favorecer u oponernos a esta flexibilidad?* 


### Buenas prácticas en el diseño de bibliotecas

Las bibliotecas de código suelen ser más útiles si son flexibles. No restrinjas las opciones innecesariamente. Con mayor flexibilidad suele venir asociada una mayor potencia.

