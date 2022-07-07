# Listas

O Python possui algumas diferentes estruturas de dados utilizados para armazenar diferentes tipos de dados. Cada um deles tem suas particularidades. 

### Criação de Listas

Para criar uma lista é necessario apenas usar colchetes:

```python
nomes = [ 'Pamela', 'Thiago', 'Celeste' ]
numeros = [ 39, 38, 42, 65, 111]
```

As vezes podemos criar listas com a ajuda de outros métodos. Por exemplo, os elementos de um string podem ser separados e cria uma listautilizando o método `split()`:

```python
>>> line = 'Pera,100,490.10'
>>> row = line.split(',') #A virgula representa o elemento de referencia para separar o string
>>> row
['Pera', '100', '490.10']
>>>
```

### Operações com listas

As listas podem armazenar varios tipos de elementos. Ainda, podemos adicionar novos elementos utilizando `append()`:

```python
nomes.append('Maira')     # O coloca ao final da lista
```

Podemos concatenar as listas usando o símbolo `+`:

```python
s = [1, 2, 3]
t = ['a', 'b']
s + t           # [1, 2, 3, 'a', 'b']
```
![](/src_aulas/Notas/01_Introducao/lista_ordem.png)

As listas tem indices que começam desde o 0.

```python
nombres = [ 'Rosa', 'Manuel', 'Luciana' ]

nombres[0]  # 'Rosa'
nombres[1]  # 'Manuel'
nombres[2]  # 'Luciana'
```

Os indices negativos iciam desde o final.

```python
nombres[-1] # 'Luciana'
```

É possivel trocar os elementos de uma lista.

```python
nomes[1] = 'Juan Manuel'
nomes                     # [ 'Rosita', 'Juan Manuel', 'Luciana' ]
```

Podemos colocar novos elementos em possições específicas da lista.

```python
nomes.insert(2, 'Iratxe') # Insere o string na possição 2 da lista. 
nomes.insert(0, 'Iratxe') # Insere o string como primeiro elemento. 
```


A função `len` retorna a longitude da lista.

```python
nomes = ['Rosa','Manuel','Luciana']
len(nomes)  # 3
```

Test de pertenência (`in`, `not in`).

```python
'Rosa' in nomes     # True
'Diego' not in nomes  # True
```

Replicar uma lista (`s * n`).

```python
s = [1, 2, 3]
s * 3   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### Iteradores de listas e busqueda

Utiliza o comando `for` para iterar sobre os elementos de uma lista.

```python
for nome in nomes:
    # usa nome
    # e.g. print(nome)
    ...
```

Para encontrar a posición de un elemento de forma rapida, usa `index()`.

```python
nomes = ['Rosa','Manuel','Luciana']
nomes.index('Luciana')   # 2
```

Si o elemento se repete mais de uma vez, `index()` retorna o indice da primeira aparição. Mas, se não esta presente gera uma excepção do tipo `ValueError`.

### Apagar elementos

Podemos apagar elemetos da lista utilizando o valor da possição ou o valor do elemento:

```python
# Usando o valor do elemento
nomes.remove('Luciana')

# Usando la possição
del nomes[1]
```


### Ordenar uma lista

Podemos ordenar as listas sem precisar da criação de uma lista nova.

```python
s = [10, 1, 7, 3]
s.sort()                    # [1, 3, 7, 10]

# Ordem invertido
s = [10, 1, 7, 3]
s.sort(reverse=True)        # [10, 7, 3, 1]

# Funciona para outros tipos
s = ['foo', 'bar', 'spam']
s.sort()                    # ['bar', 'foo', 'spam']
```

Usa a função `sorted()` para gerar uma lista nova com os dados ordenados da lista incial.

```python
t = sorted(s)               # mantem a lista s, t salva os valores ordenados
```

### Listas y matemática

*Cuidado: As listas não entendem as operações matemáticas como outros.*

```python
>>> nums = [1, 2, 3, 4, 5]
>>> nums * 2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> nums + [10, 11, 12, 13, 14]
[1, 2, 3, 4, 5, 10, 11, 12, 13, 14]
```

As listas não são vetores ou matrices, como em MATLAB, Octave, R, etc. Para esse tipo de trabalho é altamente recomendado o uso do [numpy](https://numpy.org).

