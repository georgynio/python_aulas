# Números

Nessa seção iremos aprender o uso do Python aplicado às operações matemáticas.

### Tipos de números

O Python tem 4 tipos de números:

* Booleanos
* Inteiros
* Ponto flutuante
* Números Complexos (com parte real e imaginária)

### Booleanos (bool)
Os números boleanos podem tomar um dos valores: `True` ou `False`.

```python
a = True
b = False
```

Outra forma de representar o booleano são os valores `1` e `0`. Graças a esta caracteristica podemos usa-los em algumas operaçãoes.

```python
c = 4 + True # 5
d = False
if d == 0:
    print('d is False')
```


### Inteiros (int)

Podemos representar tanto numeros positivos quanto negativos:

```python
a = 524
b = -15487935649872655
```
Representação em bases difrentes:
```python
c = 0x7fa8      # Hexadecimal
d = 0o253       # Octal
e = 0b10001111  # Binario
```

Operacões suportadas:

```
x + y      Adição
x - y      Substração
x * y      Multiplicação
x / y      Divisão (retorna um float)
x // y     Divisão inteira (retorna um int)
x % y      Módulo (retorna o resto)
x ** y     Exponenciação
abs(x)     Valor absoluto
```



### Ponto flutuante (float)

O Python representa adequadamente numeros decimais e ainda aceita o uso da notação cientifica:

```python
a = 37.45
b = 4e5 # 4 x 10**5 o 400,000
c = -1.345e-10
```

Devemos ter cuidado ao realizar algumas operações, pois, as operações de ponto flutuante não são exatos.

```python
>>> a = 2.1 + 4.2
>>> a == 6.3
False
>>> a
6.300000000000001
>>>
```

Isto não é exclusivo do Python, mas sim da computação e de como ela lida com números de ponto flutuante. Os computadores não conseguem representar com precisão exata algumas frações (como 0.98 e 0.1). Desse modo, números de ponto flutuante são automaticamente arredondados para o mais próximo que se encaixe na possibilidade do binário, o que resulta em um pequeno erro de precisão.

*No geral, esse erro é muito pequeno para ser considerado relevante, mas há situações em que não podemos desconsiderá-lo.*

Operações comuns:

```
x + y      Adição
x - y      Substração
x * y      Multiplicação
x / y      Divisão (retorna um float)
x // y     Divisão inteira (retorna um int)
x % y      Módulo (retorna o resto)
x ** y     Potência
abs(x)     Valor absoluto
```

Normalmente o Python consegue realizar esses calculos sem problemas, porém, calculos mais complexos são auxiliados com o módulo `math`.

```python
import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
```

Este modulo administra algumas constantes universais ( por exemplo: `math.e`, `math.pi`), entre outros.


### Sinais de Comparação

Estes retornam `True` ou `False`, indicando se a comparação é Verdadeira ou Falsa:

```
x < y      Menor que
x <= y     Menor ou igual a
x > y      Maior que
x >= y     Maior ou igual a
x == y     Igual a
x != y     Diferente de
```

**Nota:** o `==` é usado para avaliar a igualdade de 2 elementos entanto o `=` se usa para asignar um valor a uma variável.


Ainda temos as expresões booleanas:

`and`, `or`, `not`

Podem ser usados em alguns casos:

```python
if b >= a and b <= c:
    print('b está entre a e c')

if not (b < a or b > c):
    print('b continua estando entre a e c')
```

### Conversão de números

Os tipos de dados do Python podem ser trocados indo de decimal para inteiro ou contrario:

```python
a = int(x)    # Convertir x a int
b = float(x)  # Convertir x a float
```

Faz o teste.

```python
>>> a = 3.14159
>>> int(a)
3
>>> b = '3.14159' # Funciona também com as cadeias que representam números.
>>> float(b)
3.14159
>>>
```

**Nota:** a separação decimal é componto (.), pelo que se colocamos de forma errada o Python retornara uma mensagem de erro. Por exemplo `float(3,141592)` retorna um erro `ValueError`.



Retono ao [sumario](/Notas/01_Introducao/00_Resumo.md)