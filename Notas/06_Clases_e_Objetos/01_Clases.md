# Clases

Nesta seção veremos o conceito de classe, como criar novos tipos de objetos, sua utilidade e as vantagens desta forma de organizar programas.

## Programação Orientada a Objetos (POO)

Programação orientada a objetos é um paradigma de programação baseado no conceito de "objetos", que podem conter dados na forma de campos, também conhecidos como atributos, e códigos, na forma de procedimentos, também conhecidos como métodos.

Você já usou objetos durante o curso inúmeras vezes. Por exemplo, ao manipular uma lista.

``` python
>>> nums = [1, 2, 3]
>>> nums.append(4) # Este é um método de lista
>>> nums.insert(1,10) # Outro método
>>> nums
[1, 10, 2, 3, 4] # Estes são os dados modificados pelos métodos
>>>
```

Vamos dar uma olhada neste trecho de código. Sabemos que `nums` é uma variável do tipo list. De forma equivalente, podemos dizer que `nums` é uma *instância* da classe *list*. Cada variável do tipo list é uma instância da mesma classe.

> Quando falamos de 'instância' nos referimos a um 'objeto' (um objeto é uma instância de uma classe).

Um objeto do tipo list possui atributos (dados) e métodos.
Métodos, como `append()` ou `insert()`, são definidos quando a classe é definida, mas são usados ​​para manipular os dados de um objeto em particular (`nums` neste caso).

Podemos verificar os métodos usando a função `dir()`.

```python
# verificando os métodos de um inteiro
>>> dir(5)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

# verificando os métodos de um string
>>> dir('5')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
```

### A instrução `class`

Para definir um novo tipo de objeto, use a instrução `class`.

``` python
class Jogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.saude = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def machucado(self, pts):
        self.health -= pts
```

Um objeto do tipo `Jogador` possui atributos `x`, `y` e `health`. Seus métodos são `move()` e `machucado()`.

- Uma classe pode ser considerada a definição formal das relações entre os dados e os métodos que os manipulam.
- Um objeto é uma instância particular da classe à qual pertence, com seus próprios dados, mas os mesmos métodos que os outros objetos dessa classe.

### Instâncias

Os programas manipulam instâncias individuais de classes. Cada instância é um objeto, e é em cada objeto que se pode manipular dados e chamar seus métodos.

Você pode criar um objeto chamando a classe como se fosse uma função.

``` python
>>> a = Jogador(2, 3) # Classe de jogador definida acima
>>> b = Jogador(10, 20)
>>>
```

`a` e `b` são instâncias de `Jogador` definidas acima. Ou seja, a e b são objetos da classe `Jogador`.

**Importante:** *A instrução `class` é apenas a definição de uma classe, ela não **faz** nada sozinha. É semelhante a definir uma função.*

### Dados de uma instância

Cada instância tem seus próprios dados locais.
Aqui pedimos para ver o atributo `x` de cada instância:

``` python
>>> a.x
2
>>> b.x
10
```

Esses dados locais são inicializados, para cada instância, durante a execução do método `__init__()` da classe.

``` python
class Jogador:
    def __init__(self, x, y):
        # Todos os dados armazenados em `self` pertencem a essa instância
        self.x = x
        self.y = y
        self.saude = 100
```

Não há restrições quanto ao número ou tipo de atributos que uma classe pode ter.

### Métodos de uma instância

Os métodos de uma instância são os métodos e funções que atuam nos dados armazenados nessa instância.

``` python
class Jogador:
    ...
    # `move` é um método
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

Veja como funciona:

``` python
>>> a.move(1, 2)

# `self` se refere a `a`
# `dx` refere-se a `1`
# `dy` refere-se a `2`
def move(self, dx, dy):
    ...
```

Por convenção, sempre chamamos a instância atual de `self`, e ela sempre é passada como o primeiro argumento para todos os métodos. **O nome real da variável realmente não importa**, mas é uma convenção em Python chamar o primeiro argumento de `self`.

Poderíamos usar `mesmo`, por exemplo, em vez de `self` e tudo funcionará sem problemas:

``` python
jogador da classe:
    ...
    # `mover` é um método
    def move(mesmo, dx, dy):
        mesmo.x += dx
        mesmo.y += dy
```

### Visibilidade nas classes (Scoping)

As classes não restringem um ambiente de visibilidade para os métodos.

``` python
class Jogador:
    ...
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

     def left(self, dist):
         move(-dist, 0) # CUIDADO! Refere-se a uma função global `move`.
         self.move(-dist, 0) # Sim. Chama o método `move` definido acima.
```

Se você precisa se referir a um dado ou método de uma classe você tem que fazer uma referência explícita (adicionando o `self`), caso contrário você está se referindo a outra coisa como no exemplo acima.

## Retono ao [sumario](./00_Resumo.md)