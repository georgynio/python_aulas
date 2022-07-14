# Compreensão da lista


*List comprehension* foi concebida na [PEP 202](https://peps.python.org/pep-0202/) e é uma forma concisa de criar e manipular listas. Sua sintaxe básica é:

```python
[<expressão> for <item> in <lista>]
```

Em outras palavras: aplique a `expressão` em cada `item` da `lista`.

## Criar novas listas

A compreensão de lista cria uma nova lista aplicando uma operação a cada elemento de uma sequência.

``` python
>>> para = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a]
>>> b
[2, 4, 6, 8, 10]
>>>
```

Outro exemplo:

``` python
>>> nomes = ['Edmundo', 'Jane']
>>> a = [name.lower() for name in names]
>>> para
['edmundo', 'juana']
>>>
```

A sintaxe geral é: `[<expressão> for <variável> in <sequência>]`.

## Filtros

A compreensão da lista pode ser usada para filtragem.

``` python
>>> para = [1, -5, 4, 2, -2, 10]
>>> b = [2*x for x in a if x > 0]
>>> b
[2, 8, 4, 20]
>>>
```

## Casos de uso

A compreensão da lista é extremamente útil. Por exemplo, você pode coletar os valores de um campo específico de um dicionário:

``` python
frutas = [s['name'] for s in truck]
```

Ou você pode fazer consultas (*consultas*) como se as sequências fossem bancos de dados.

``` python
a = [s for s in caminhao if s['price'] > 100 e s['crates'] > 50]
```

Você também pode combinar compreensão de lista com redução de sequência:

``` python
cost = sum([s['crates']*s['price'] for s in truck])
```

## sintaxe geral da compreensão de lista e sequência

```python
[<expressão> for <variável> in <sequência> if <condição>]
```

O que significa

``` python
resultado = []
for variavel in sequencia:
    if condicao:
        resultado.append(expressao)
```

## Contexto histórico

A compreensão de listas vem da matemática (definição de conjuntos por compreensão).

``` bash
a = [x * x for x in s if x > 0] # Python

a = {x^2 | x ∈ s, x > 0} # Matemática
```

A maioria dos programadores não costuma pensar no lado matemático dessa ferramenta. Podemos vê-lo simplesmente como uma abreviação sofisticada para definir listas.

## Retono ao [sumario](./00_Resumo.md)