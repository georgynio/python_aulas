# Métodos especiais

Aqui veremos como modificar varios comportamentos do Python fazendo uso dos "métodos especiais".

## Introdução

Uma classe pode ter métodos especiais definidos. Esses métodos têm um significado particular para o interpretador Python. Seus nomes começam e terminam com `__` (sublinhado duplo). Por exemplo `__init__`.

``` python
class Lote(objeto):
    def __init__(self):
        ...
    def __repr__(auto):
        ...
```

Existem dezenas de métodos especiais, depende da função, mas vamos lidar apenas com alguns exemplos específicos aqui. Para ter uma ideia podemos usar a funçao `dir()`.

```python
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

```

## Métodos especiais para converter em strings

Os objetos têm duas representações do tipo string.

``` python
>>> from datetime import date
>>> d = date(2020, 12, 21)
>>> print(d)
21-12-2020
>>> d
datetime.date(2020, 12, 21)
>>>
```

A função `str()` é usada para criar uma representação bonita:

``` python
>>> str(d)
'2020-12-21'
>>>
```

Mas para criar uma representação mais informativa para programadores, a função `repr()` é usada.

``` python
>>> repr(d)
'datetime.date(2020, 12, 21)'
>>>
```

As funções `str()` e `repr()` chamam métodos especiais da classe para gerar a string a ser exibida.

``` python
class Date(objeto):
    def __init__(self, ano, mês, dia):
        self.ano = ano
        self.mês = mês
        self.day = dia

    # Com `str()`
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # Com `repr()`
    def __repr__(auto):
        return f'Data({self.year},{self.month},{self.day})'
```

*Nota: Existe uma convenção para `__repr__()` que indica que deve retornar uma string que, quando passada para `eval()`, recrie o objeto subjacente. Dê uma olhada no exemplo `datetime.date(2020, 12, 21)`. Se não for possível criar uma string que faça isso, a convenção é gerar uma representação que seja fácil de interpretar.*

``` python
class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Usado com `repr()`
    def __repr__(auto):
        return f'Ponto({self.x}, {self.y})'
```

## Métodos matemáticos especiais

As operações matemáticas envolvem chamadas para os métodos a seguir.

``` python
a + b   a.__add__(b)
a - b   a.__sub__(b)
a * b   a.__mul__(b)
a / b   a.__truediv__(b)
a // b  a.__floordiv__(b)
a % b   a.__mod__(b)
a << b  a.__lshift__(b)
a >> b  a.__rshift__(b)
a & b   a.__and__(b)
a | b   a.__or__(b)
a ^ b   a.__xor__(b)
a ** b  a.__pow__(b)
-a      a.__neg__()
~a      a.__invert__()
abs(a)  a.__abs__()
```

Assim, definir um método `__add__(b)` na classe `Ponto`, por exemplo, nos permitirá adicionar duas instâncias desta classe usando o operador `+`.

``` python
class Ponto():
    ...
    ...
    def __add__(self, b):
      return Point(self.x + b.x, self.y + b.y)
```

Como no exemplo a seguir:

``` python
>>> a = Ponto(1,2)
>>> b = Ponto(3,4)
>>> repr(a + b)
'Ponto(4, 6)'
```


## Métodos especiais para acessar elementos

Os métodos a seguir são usados ​​para implementar contêineres:

``` python
len(x)      x.__len__()
x[a]        x.__getitem__(a)
x[a] = v    x.__setitem__(a,v)
del x[a]    x.__delitem__(a)
```

Você pode implementá-los em suas classes.

``` python
class sequencia:
    def __len__(self):
        ...
    def __getitem__(self,a):
        ...
    def __setitem__(self,a,v):
        ...
    def __delitem__(self,a):
        ...
```

## métodos de chamada

O processo de chamar um método pode ser dividido em duas partes:

1. Pesquisa: O operador `.` é usado
2. Chamada: `()` são usados

``` python
>>> m = Lote('Pera', 100, 490,10)
>>> c = m.cost # Pesquisa
>>> c
<bound method Lote.custo of <Lote object at 0x590d0>>
>>> c() # Chamado
49010.0
>>>
```

*Observação*: a resposta à solicitação de renderização `c` é algo como
<Método Lote.custo associado a <objeto Lote em 0x590d0>>*

## Acesso aos atributos

Existe uma maneira alternativa de acessar, manipular e gerenciar os atributos de um objeto.

``` python
getattr(obj, 'nome') # Equivalente a obj.nome
setattr(obj, 'nome', value) # Equivalente a obj.nome = value
delattr(obj, 'name') # Equivalente a del obj.name
hasattr(obj, 'name') # Verifica se a propriedade existe
```

Exemplo:

``` python
if hasattr(obj, 'x'):
    x = getattr(obj, 'x'):
else:
    x = None
```

*Nota*: se `getattr()` não encontrar o atributo procurado (`x` neste exemplo), ele retorna o argumento opcional *arg* (`None` neste caso)

``` python
x = getattr(obj, 'x', None)
```

## Retono ao [sumario](./00_Resumo.md)