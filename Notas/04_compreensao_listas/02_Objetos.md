# Objetos

Nesta seção, discutimos alguns problemas relacionados ao gerenciamento de memória, cópias de variáveis ​​e verificação de tipos.

## Atribuições

A atribuição de valores é a passagem de informação a determinada variável. A linguagem Python tem definido que o sinal que conhecemos pelo nome de igual (=) será o operador de atribuição.

A estrutura de uma atribuição é a seguinte:

```python
<variável> = <valor>
```

Muitas operações em Python estão relacionadas a *atribuir* ou *salvar* valores.

``` python
a = valor # Atribuição a uma variável
s[n] = valor # Atribuição a uma lista
s.append(value) # Anexa a uma lista
d['key'] = value # Adicionar ao dicionário
```

*Aviso: **nunca faça uma cópia** do valor atribuído.*
As atribuições são simplesmente cópias das referências (ou cópias do ponteiro, se preferir).

## Exemplo de atribuição

Considere este trecho de código.

``` python
a = [1,2,3]
b = a
c = [a,b]
```

Isso significa que modificar um valor modifica *todas* as referências.

``` python
>>> a.append(999)
>>> a
[1,2,3,999]
>>> b
[1,2,3,999]
>>>c
[[1,2,3,999], [1,2,3,999]]
>>>
```

Observe como uma mudança na lista original aciona mudanças em todas as outras variáveis ​​(ai!). Isso ocorre porque nenhuma cópia foi feita. Todos são indicadores da mesma coisa.

## Reatribuir valores

A reatribuição de valor *nunca* substitui a memória ocupada por um valor anterior.

``` python
a = [1,2,3]
b = a
a = [4,5,6]

print(a) # [4, 5, 6]
print(b) # [1, 2, 3] Mantém o valor original
```

Lembre-se: **Variáveis ​​são nomes, não locais na memória.**

## Perigos

Se eles não explicarem isso para você, mais cedo ou mais tarde isso lhe trará problemas. Um exemplo típico é quando você altera um dado pensando que é uma cópia privada e isso inadvertidamente corrompe os dados em outra parte do programa.

*Comentário: Esta é uma das razões pelas quais os tipos de dados primitivos (int, float, string) são imutáveis ​​(somente leitura).*

## Identidade e referências

```bash
Em python, uma variável é apenas um NOME que REFERENCIA a um OBJETO.
```

Você pode usar o operador `is` para verificar se dois valores correspondem ao mesmo objeto.

``` python
>>> para = [1,2,3]
>>> b = a
>>> a is b
True
>>>
```

`is` compara a identidade do objeto (que é representado por um inteiro). Essa identidade também pode ser obtida usando `id()`.

``` python
>>> id(a)
3588944
>>> id(b)
3588944
>>>
```

Observação: Para ver se dois valores são iguais, é melhor usar o `==`. O comportamento de `is` pode dar resultados inesperados:

``` python
>>> para = [1,2,3]
>>> b = a
>>> c = [1,2,3]
>>> a is b
True
>>> a is c
False
>>> a == c
True
>>>
```

## Cópias rasas

Listas e dicionários têm métodos para fazer cópias (não apenas referências, mas duplicatas):

``` python
>>> a = [2,3,[100,101],4]
>>> b = list(a) # Faça uma cópia
>>> a is b
False
```

Agora `b` é uma nova lista.

``` python
>>> a.append(5)
>>> a
[2, 3, [100, 101], 4, 5]
>>> b
[2, 3, [100, 101], 4]
```

Apesar disso, os elementos de `a` e `b` ainda são compartilhados.

``` python
>>> a[2].append(102)
>>> b[2]
[100.101.102]
>>>
>>> a[2] is b[2]
True
>>>
```

Neste exemplo, a lista interna `[100, 101, 102]` é compartilhada por ambas as variáveis. A cópia que fizemos com o comando `b = list(a)` é uma *cópia superficial*.
Olhe para este gráfico.

![cópias rasas](shallow.png)

A lista interna ainda é compartilhada.

## Cópias profundas

Às vezes, você precisará fazer uma cópia de um objeto, bem como de todos os objetos que ele contém. Chamamos isso de *cópia profunda*. Você pode usar a função `deepcopy` do módulo `copy` para isso:

``` python
>>> a = [2,3,[100,101],4]
>>> import copy
>>> b = copy.deepcopy(a)
>>> a[2].append(102)
>>> b[2]
[100,101]
>>> a[2] is b[2]
False
>>>
```

## Nome, valores e tipos

Os nomes de variáveis ​​não têm um tipo associado. São apenas nomes. Mas os valores têm um tipo subjacente.

``` python
>>> a = 42
>>> b = 'Olá Mundo'
>>> type(a)
<class 'int'>
>>> type(b)
<class 'str'>
```

`type()` informa o tipo do valor.

## Verificação de tipo

Você pode verificar se um objeto é uma instância de um determinado tipo.

``` python
if isinstance(a, list):
    print('a é uma lista')
```

Ou mesmo se o seu tipo estiver entre vários tipos.

``` python
if isinstance(a, (lista,tupla)):
    print('para uma lista ou tupla')
```

*Cuidado: Muitas verificações de tipo podem resultar em código excessivamente complexo. Você normalmente o usa para evitar erros comuns cometidos por outros usuários do seu código.*

## Tudo é um objeto

Números, strings, listas, funções, exceções, classes, instâncias, etc. são todos objetos. Isso significa que eles podem ser nomeados, podem ser passados ​​como dados, colocados em contêineres, etc. sem restrições. Não há objetos especiais em Python. Todos os objetos viajam de primeira classe.

Um exemplo simples:

```python
>>> import math
>>> items = [abs, math, ValueError ]
>>> items
[<built-in function abs>,
  <module 'math' (builtin)>,
  <type 'exceptions.ValueError'>]
>>> items[0](-45)
45
>>> items[1].sqrt(2)
1.4142135623730951
>>> try:
        x = int('not a number')
    except items[2]:
        print('Failed!')
Failed!
>>>
```

Aqui, `items` é uma lista que tem uma função, um módulo e uma exceção. Sim, este é um exemplo raro. Mas afinal é um exemplo. Você pode usar os elementos da lista em vez dos nomes originais:

``` python
items[0](-45) # abs
items[1].sqrt(2) # matemática
exceto items[2]: # ValueError
```

Com grandes poderes sempre vem grandes responsabilidades. Só porque você pode não significa que você deve fazer esse tipo de coisa.

## Retono ao [sumario](./00_Resumo.md)