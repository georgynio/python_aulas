# Herança

A Herança é um conceito do paradigma da orientação à objetos que determina que uma classe pode herdar atributos e métodos de uma outra classe e, assim, evitar que haja muita repetição de código.

## Introdução

A herança é usada para criar objetos mais especializados a partir de objetos existentes.

``` python
class Pai:
    ...

class Filho(Pai):
    ...
```

`Filho` é dito ser uma classe ou subclasse derivada. A classe `Pai` é conhecida como classe base ou superclasse. A expressão `class Filho(Pai):` significa que estamos criando uma classe chamada `Filho` que é derivada da classe `Pai`.

## Extensões

Usando herança, você pode pegar uma classe existente e:

* Adicionar métodos
* Redefinir métodos existentes
* Adicionar novos atributos

Você pode vê-lo como uma forma de **estender** seu código existente. Embora tenha muitas vantegens, **tenha cuidado com os novos comportamentos**.

## Exemplo

Suponha que você comece com a seguinte classe:

``` python
class Lote:
    def __init__(self, nome, caixoes, preco):
        self.name = nome
        self.caixoes = caixoes
        self.preco = preco

    def custo(self):
        return self.caixoes * self.preco

    def vender(self, ncaixoes):
        self.caixoes -= ncaixoes
```

Você pode modificar o que precisa por herança.

## Adicionar um novo método

``` python
class MeuLote(Lote):
    def doar(self):
        self.vender(self.caixoes)
```

Pode ser usado assim:

``` python
>>> c = MeuLote('Pera', 100, 490,1)
>>> c.vender(25)
>>> c.caixoes
75
>>> c.doar()
>>> c.caixoes
0
>>>
```

Esta classe herdou os atributos e métodos de `Lote` e o estendeu com um novo método (`doar()`).

## Redefina um método existente

``` python
class MeuLote(Lote):
    def custo(proprio):
        return 1.25 * self.caixoes * self.price
```

Um exemplo de uso:

``` python
>>> c = MeuLote('Pera', 100, 490,1)
>>> c.custo()
61262,5
>>>
```

## Use um método predominante

Há momentos em que uma classe estende o método da superclasse à qual pertence, mas precisa executar o método original como parte da substituição do novo método. Para se referir à superclasse, use `super()`:

``` python
class Lote:
    ...
    def custo(self):
        return self.caixoes * self.price
    ...

class MeuLote(Lote):
    def custo(self):
        # Observe como usamos `super`
        custo_original = super().custo()
        return 1,25 * custo_original
```

Use `super()` para chamar o método da classe base (da qual ele herda).

## O método `__init__` e herança.

A criação de cada instância executa `__init__`. Aí está o código importante para criar uma nova instância. Se você substituir `__init__` sempre inclua uma chamada para o método `__init__` da classe base para inicializá-lo também.

``` python
class Lote:
    def __init__(self, nome, caixoes, preço):
        self.name = nome
        self.caixoes = caixoes
        self.preco = preco
    ...


class MeuLote(Lote):
    def __init__(self, name, caixoes, preco, fator):
        # Observe como a chamada para `super().__init__()` é
        super().__init__(nome, buckets, preco)
        self.fator = fator

    def custo(self):
        return self.fator * super().custo()
```

Você precisa chamar o método `__init__()` na classe base. É uma maneira de executar a versão anterior do método que estamos substituindo, como acabamos de mostrar.

## A classe base `object`

Se uma classe não tem superclasse, `object` às vezes é escrito como a classe base.

``` python
class Figura_geom(object):
     ...
```

`object` é a superclasse de cada objeto em Python.

## herança múltipla

Você pode herdar de várias classes simultaneamente se as especificar na definição de classe.

``` python
class Mae:
     ...

class Pai:
     ...

class Filho (Mae, Pai):
     ...
```

A classe `Filho` herda características de ambos os pais. 

## Retorno ao [sumário](./00_Resumo.md)