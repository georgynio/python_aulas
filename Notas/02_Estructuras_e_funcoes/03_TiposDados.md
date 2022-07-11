# Tipos e estruturas de dados

Esta seção apresenta duas estruturas de dados elementares: tuplas e dicionários.

## Tipos de dados primitivos

Python tem poucos tipos de dados primitivos.

* Números inteiros
* Números de ponto flutuante
* Cadeias de texto

Já sabemos algo sobre esses tipos de dados do capítulo anterior.

## Tipo None

``` python
email_address = None
```

`None` é frequentemente usado como um curinga para reservar o lugar para um valor opcional ou ausente. Em condicionais, ele é avaliado como 'False'.

``` python
if email_address:
    send_email(email_address, msg)
```

## Estruturas de dados

Programas reais têm dados mais complexos do que podemos armazenar em tipos primitivos. Por exemplo, informações sobre um pedido de frutas:

``` código
100 caixas de maçãs a $ 490,10 cada
```

Podemos ver isso como um "objeto" com três partes:

* Nome da mercadoria ("Maçãs", uma string)
* Número ou quantidade (100, um número inteiro)
* Preço (490,10, um float)

## Tuplas

Uma tupla é uma coleção com valores agrupados.

Exemplo:

``` python
s = ('Maçãs', 100, 490,1)
```

Tuplas são frequentemente usadas para representar registros ou estruturas *simples*.
Normalmente, uma tupla representa um único *objeto* com várias partes. Uma analogia possível é a seguinte: *Uma tupla é como uma linha em um banco de dados*.

O conteúdo de uma tupla é ordenado (como em uma lista).

``` python
s = ('Maçã', 100, 490,1)
nome = s[0] # 'Apple'
quantidade = s[1] # 100
preço = s[2] # 490,1
```

O conteúdo das tuplas não pode ser modificado.

``` python
>>> s[1] = 75
TypeError: objeto não suporta atribuição de item
```

Você pode, no entanto, fazer uma nova tupla com base no conteúdo de outra, o que não é o mesmo que modificar o conteúdo.

``` python
s = (s[0], 75, s[2])
```

### Pacote de tuplas

Tuplas são frequentemente usadas para empacotar informações relacionadas em uma única *entidade*.

``` python
s = ('Maçãs', 100, 490,1)
```

Uma tupla pode ser passada de um lugar para outro em um programa como um único objeto.

### Descompacte tuplas

Para usar uma tupla em outro lugar, devemos descompactar seu conteúdo em diferentes variáveis.

``` python
frutas, caixas, preço = s
print('Custo:', gavetas * preço)
```

O número de variáveis ​​à esquerda deve ser consistente com a estrutura da tupla.

``` python
nome, gavetas = s # ERRO
Traceback (última chamada mais recente):
...
ValueError: muitos valores para descompactar
```

## Tuplas vs. listas

Tuplas parecem ser listas somente leitura. No entanto, as tuplas são frequentemente usadas para um único item que consiste em várias partes, enquanto as listas são frequentemente usadas para uma coleção de itens diferentes, geralmente do mesmo tipo.

``` python
record = ('Maçãs', 100, 490.1) # Uma tupla representando um registro dentro de um pedido de frutas

símbolos = [ 'Maçãs', 'Peras', 'Tangerinas' ] # Uma lista representando três frutas diferentes.
```

## Dicionários

Um dicionário é uma função que envia *chaves* para *valores*. As chaves servem como índices para acessar os valores.

``` python
s = {
    'fruta': 'maçã',
    'gavetas': 100,
    'preço': 490,1
}
```

## Operações usuais

Para obter o valor armazenado em um dicionário usamos as chaves.

``` python
>>> print(s['fruta'], s['caixas'])
maçãs 100
>>> s['preço']
490,10
>>>
```

Para adicionar ou modificar valores, simplesmente atribuímos usando a chave.

``` python
>>> s['gavetas'] = 75
>>> s['data'] = '08/06/2020'
>>>
```

para deletar um valor, usamos o comando `del`.

``` python
>>> del s['data']
>>>
```

## Por que dicionários?

Os dicionários são úteis quando existem *muitos* valores diferentes e esses valores podem ser modificados ou manipulados. Como o acesso aos elementos é feito por *chave*, não é necessário lembrar uma posição para determinados dados, o que muitas vezes cumpre um objetivo fundamental: tornar o código mais legível (e, portanto, menos propenso a erros).

``` python
s['price'] # dicionário
#vs
s[2] # lista
```

Retono ao [sumario](/Notas/02_Estructuras_e_funcoes/00_Resumo.md)