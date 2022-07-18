# Sequências

Um tipo `sequencial` é um que suporta o operador de associção (`in`), da função de tamanho (`len()`), fatias (`[]`) e é iterável.

## Tipo de sequências

Python tem três tipos de dados que são *sequências*.

* String: `'Olá'`. Uma string é uma sequência de caracteres.
* Lista: `[1, 4, 5]`.
* Tupla: `('Pera', 100, 490,1)`.

Todas as sequências têm uma ordem, indexadas por números inteiros, e têm um comprimento.

``` python
a = 'Hello' # String
b = [1, 4, 5] # Lista
c = ('Pera', 100, 490,1) # Tupla

# Pedido indexado
a[0] # 'H'
b[-1] # 5
c[1] # 100

# comprimento das sequências
len(a) # 5
len(b) # 3
len(c) # 3
```

As sequências podem ser replicadas: `s * n`.

``` python
>>> para = 'Olá'
>>> a *3
'Ola Ola Ola'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

Sequências do mesmo tipo também podem ser concatenadas: `s + t`. Porém, não devemos misturar os tipos.

``` python
>>> para = (1, 2, 3)
>>> b = (4, 5)
>>> a + b
(1, 2, 3, 4, 5)
>>>
>>> c = [1, 5]
>>> a + c
Traceback (última chamada mais recente):
  Arquivo "<stdin>", linha 1, em <module>
TypeError: só pode concatenar tupla (não "lista") para tupla
```

## Fatias (slicing)

Pegar uma fatia é pegar uma subsequência de uma sequência.
A sintaxe é `s[start:end]`, onde `start` e `end` são os índices da subsequência que você deseja.

``` python
a = [0,1,2,3,4,5,6,7,8]

a[2:5] # [2,3,4]
a[-5:] # [4,5,6,7,8]
a[:3] # [0,1,2]
```

* Os índices `start` e `end` devem ser inteiros.
* Fatias *não* incluem o valor final. É como os intervalos semiabertos na matemática.
* Se os índices forem omitidos, eles assumem seus valores padrão: o início ou o fim da lista.

## Reatribuição de fatias

Nas listas, uma fatia pode ser reatribuída ou excluída.

``` python
# Reatribuição
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12] # [0,1,10,11,12,4,5,6,7,8]
```

*Observação: a fatia realocada não precisa necessariamente ter o mesmo comprimento.*

```python
# Eliminación
a = [0,1,2,3,4,5,6,7,8]
del a[2:4]                # [0,1,4,5,6,7,8]
```

## Reduções de sequência

Existem algumas operações comuns que reduzem uma sequência a um único valor.

``` python
>>> s = [1, 2, 3, 4]
>>> sum(s)
10
>>> min(s)
1
>>> max(s)
4
>>> t = ['Olá', 'Mundo']
>>> max(t)
'Mundo'
>>>
```

## Iterar sobre uma sequência

Os loops `for` iteram sobre os elementos de uma sequência.

``` python
>>> s = [1, 4, 9, 16]
>>> for i in s:
...    print(i)
...
1
4
9
16
>>>
```

A cada iteração do loop, você obtém um novo elemento para trabalhar. A variável iteradora assumirá esse novo valor. No exemplo a seguir, a variável do iterador é `x`:

``` python
for x in s: # `x` é uma variável iteradora
    ...instruções
```

A cada iteração, o valor anterior da variável (se houver) é substituído. Depois que o loop termina, a variável iteradora salva o ultimo valor.

## O comando break

Você pode usar o comando `break` para quebrar um loop mais cedo.

``` python
for nome in lista_nomes:
    if nome == 'Joana':
        break
    ...
    ...
instruções
```

Quando o comando `break` é executado, ele sai do loop e passa para as próximas `instruções`. O comando `break` só se aplica ao loop mais interno. Se um loop estiver aninhado em outro loop, o comando não interromperá o loop externo.

## O comando continue

Para pular um elemento e passar para o próximo, use o comando `continue`.

``` python
for linha in linhas:
    if line == '\n': # Ignora instruções que processam linhas
        continue
    # Instruções que processam linhas
    ...
```

Isso é útil quando o item encontrado não é de interesse ou precisa ser ignorado no processamento.

## Ciclos sobre inteiros

Para iterar em um intervalo de inteiros, use `range()`.

``` python
for i in range(100):
    #i = 0,1,...,99
```

A sintaxe é `range([start], [end], [step])` (o que está entre colchetes é opcional).

``` python
for i in range(100):
    #i = 0,1,...,99
    ...código
for j in range(10,20):
    #j = 10,11,..., 19
    ...código
for k in range(10,50,2):
    #k = 10,12,...,48
    # Observe que ele passa por dois.
    ...código
```

* O valor final nunca é incluído. É como com as fatias.
* `start` é opcional. Se não se indica o programa entende que é o padrão '0'.
* `step` é opcional. Se não se indica o programa entende que é o padrão é `1`.
* `range()` calcula os valores conforme você precisa deles. Na verdade, ele não armazena todo o intervalo de números na memória.

## A função enumerar()

A função `enumerate` adiciona um contador extra a uma iteração.

``` python
nomes = ['Edmundo', 'Juana', 'Rosita']
for i, nome in enumerate(nomes):
    # i = 0, nome = 'Edmundo'
    # i = 1, nome = 'Jane'
    # i = 2, nome = 'Rosita'
```

A forma geral é `enumerate(sequence [, start = 0])`. `start` é opcional.
Um bom exemplo de quando usar `enumerate()` é acompanhar o número
de linha enquanto você está lendo um arquivo:

``` python
with open(file_name) as f:
    for nline, line in enumerate(f, start=1):
        ...
```

No final do dia, `enumerate` é apenas uma boa forma abreviada de escrever:

``` python
eu = 0
for x in s:
    instruções
    eu += 1
```

Usando `enumerate` temos que digitar menos e o programa roda um pouco mais rápido.

## Tuplas e laços for

Você pode iterar com várias variáveis ​​de iteração.

``` python
pontos = [(1, 4),(10, 40),(23, 14),(5, 6),(7, 8)]
for x, y in pontos:
    # x = 1, y = 4
    # x = 10, y = 40
    # x = 23, y = 14
    #...
```

Quando você usa várias variáveis, cada tupla é *descompactada* em um conjunto de variáveis ​​de iteração. O número de variáveis ​​deve corresponder ao número de elementos em cada tupla.

## A função zip()

A função `zip` pega várias sequências e as combina em um iterador.

``` python
colunas = ['nome', 'gavetas', 'preço']
valores = ['Pera', 100, 490,1 ]
pares = zip(colunas, valores)
# ('nome','Pêra'), ('caixas',100), ('preço',490,1)
```

Para obter o resultado, você deve iterar. Você pode usar várias variáveis ​​para descompactar as tuplas como mostrado acima.

``` python
for coluna, valor in pares:
    ...
```

Um uso comum de `zip` é criar pares chave/valor e construir dicionários.

``` python
d = dict(zip(colunas, valores))
```

## Retorno ao [sumário](./00_Resumo.md)