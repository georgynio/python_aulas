# Contêineres

Nesta seção vamos lidar com listas, dicionários e conjuntos.

## Panorama

Os programas geralmente trabalham com muitos objetos.

* Um caminhão com caixas de frutas
* Uma tabela de preços de caixa de frutas

Em Python existem três opções principais para escolher.

* Listas. Dados ordenados.
* Dicionários. Dados confusos.
* Conjuntos. Coleção bagunçada de elementos únicos.

## Listas como contêineres

Use listas quando a ordem dos dados for importante. Lembre-se de que as listas podem conter qualquer tipo de objeto.
Por exemplo, uma lista de tuplas.

``` python
caminhão = [
    ('Pera', 100, 490,1),
    ('Laranja', 50, 91,3),
    ('Limão', 150, 83,44)
]

truck[0] # ('Pera', 100, 490.1)
truck[2] # ('Limão', 150, 83.44)
```

## Construindo uma lista

Como construir uma lista do zero.

``` python
registros = [] # inicia com uma lista vazia

# Usamos o .append() para adicionar elementos
records.append(('Pera', 100, 490.10))
registros.append(('Laranja', 50, 91.3))
...
```

Um exemplo de como carregar registros de um arquivo.

``` python
registros = [] # inicia com uma lista vazia

com open('../Data/truck.csv', 'rt') como f:
    next(f) # Pula o cabeçalho
    para linha em f:
        linha = linha.split(',')
        registros.append((linha[0], int(linha[1]), float(linha[2])))
```

## Dicionários como contêineres

Os dicionários são úteis se quisermos pesquisar rapidamente (por teclas).
Por exemplo, um dicionário de preços de gaveta.

``` python
preços = {
   'Pera': 513,25,
   'Limão': 87,22,
   'Laranja': 93,37,
   'Tangerina': 44,12
}
```

Assim, podemos pesquisar os dados:

``` python
>>> preços['Laranja']
93,37
>>> preços['pêra']
513,25
>>>
```

## Construção de dicionários

Exemplo de construção de um dicionário do zero.

``` python
preços = {} # Começamos com um dicionário vazio

#adiciona elementos
preços['Pera'] = 513,25
preços['Limão'] = 87,22
preços['Laranja'] = 93,37
```

Um exemplo de como construir um dicionário a partir do conteúdo de um arquivo.

``` python
preços = {} # Começamos com um dicionário vazio

com open('../Data/prices.csv', 'rt') como f:
    para linha em f:
        linha = linha.split(',')
        preços[linha[0]] = float(linha[1])
```

## Pesquisas em um dicionário

Você pode verificar se existe uma chave:

``` python
se digitar d:
    # E ISSO É
senão:
    # NÃO
```

## Teclas compostas

Quase qualquer valor pode ser usado como chave em um dicionário Python. A principal restrição é que uma chave deve ser do tipo imutável.
Por exemplo, tuplas:

``` python
feriados = {
  (1, 1): 'Ano Novo',
  (1, 5): 'Dia do Trabalho',
  (13, 9) : "Dia do Programador",
}
```

Então, podemos acessar o dicionário assim:

``` python
>>> feriados[(1, 5)]
'Dia do Trabalhador'
>>>
```

*Listas, conjuntos e dicionários não podem ser usados ​​como chaves de dicionário, pois são mutáveis.*

## Conjuntos

Um conjunto é uma coleção de elementos únicos sem ordem e sem repetição.

``` python
citrino = { 'Laranja','Limão','Tangerina' }
# Alternativamente podemos escrever assim:
cítrico = set(['Laranja', 'Limão', 'Tangerina'])
```

Os conjuntos são úteis para avaliar a associação.

``` python
>>> cítrico
set(['Laranja', 'Limão', 'Tangerina'])
>>> 'Laranja' em citrinos
Verdadeiro
>>> 'Maçã' em citrinos
Falso
>>>
```

Os conjuntos também são úteis para remover duplicatas.

``` python
nomes = ['Laranja', 'Maçã', 'Pera', 'Laranja', 'Pera', 'Banana']

unico = set(nomes)
# unique = {'Maçã', 'Banana', 'Laranja', 'Pera'}
```

Mais operações em conjuntos:

``` python
citrus.add('Banana') # Adiciona um item
citrus.remove('Lemon') # Remove um elemento

s1 | s2 # União dos conjuntos s1 e s2
s1 & s2 # Definir interseção
s1 - s2 # Diferença de conjuntos
```

## Retono ao [sumario](/Notas/02_Estructuras_e_funcoes/00_Resumo.md)