# Impressão com formato

Quando você trabalha com dados, é comum você querer imprimir uma saída estruturada (tabelas, etc.). Por exemplo:

``` código
  Preço das gavetas de nome
---------- ---------- -----------
 Lima 100 32,20
 Laranja 50 91,10
 Cáqui 150 103,44
 Tangerina 200 51,23
 Pêssego 95 40,37
 Tangerina 50 65,10
 Laranja 100 70,44
```

## Formato de string

Uma ótima maneira de formatar uma string em Python (a partir da versão 3.6) é usar `f-strings`.

``` python
>>> nome = 'Laranja'
>>> gavetas = 100
>>> preco = 91,1
>>> f'{nome:>10s} {caixas:>10d} {preco:>10.2f}'
'Laranja 100 91,10'
>>>
```

A parte `{expression:format}` será substituída. Normalmente `f-strings` são usadas com `print`.

``` python
print(f'{nome:>10s} {caixas:>10d} {preço:>10.2f}')
```

## Códigos de formato

Os códigos de formato (o que segue o `:` dentro do `{}`) são semelhantes aos usados ​​no `printf()` da linguagem C. Os mais comuns são:

``` código
d Número inteiro decimal
b inteiro binário
x Inteiro Hex
f Flutuar como [-]m.dddddd
e Flutuar como [-]m.dddddde+-xx
g Float, mas com uso seletivo da notação exponencial E.
s Correntes
c Caractere (de um inteiro, seu código)
```

Os modificadores permitem ajustar a largura a ser impressa ou a precisão decimal (número de dígitos após o ponto). Essa é uma lista parcial:

``` código
:>10d Inteiro alinhado à direita em um campo de 10 caracteres
:<10d Inteiro alinhado à esquerda em um campo de 10 caracteres
:^10d Inteiro centralizado em um campo de 10 caracteres
:0.2f Float com dois dígitos de precisão
```

## Formatação de dicionários

Você pode usar o método `format_map()` para aplicar um formato aos valores de um dicionário:

``` python
>>> s = {
    'nome': 'Laranja',
    'gavetas': 100,
    'preço': 91,1
}
>>> '{name:>10s} {crates:10d} {price:10.2f}'.format_map(s)
'Laranja 100 91,10'
>>>
```

Ele usa os mesmos códigos das `f-strings` mas pega os valores fornecidos pelo dicionário.

## O método format()

Existe um método `format()` que permite formatar argumentos.

``` python
>>> '{name:>10s} {crates:10d} {price:10.2f}'.format(name='Orange', crates=100, price=91.1)
'Laranja 100 91,10'
>>> '{:10s} {:10d} {:10.2f}'.format('Laranja', 100, 91,1)
'Laranja 100 91,10'
>>>
```

A verdade é que `format()` é um pouco longo para nós e preferimos usar `f-strings`.

## Formato estilo C

Você também pode usar o operador `%`.

``` python
>>> 'O valor é %d' % 3
'O valor é 3'
>>> '%5d %-5d %10d'% (3,4,5)
' 3. 4. 5'
>>> '%0.2f' % (3.1415926,)
'3.14'
```

Isso requer um único item ou uma tupla à direita. Os códigos também são inspirados no `printf()` de C. Tem a dificuldade que você tem que contar posições e todas as variáveis ​​vão juntas no final.

## Retono ao [sumario](/Notas/03_Dados/00_Resumo.md)