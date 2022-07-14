# estilos de codificação

## PEP 8 - O guia de estilo para Python

A comunidade de usuários do Python adotou um guia de estilo que torna o código mais fácil de ler e consistente entre programas de diferentes usuários. Este guia não é obrigatório, mas é altamente recomendado. O documento completo chama-se PEP 8 e foi escrito originalmente em [inglês](https://www.python.org/dev/peps/pep-0008/), embora haja alguma tradução para [português](https://wiki.python.org.br/GuiaDeEstilo).

Aqui está um resumo com apenas algumas recomendações.

### Recuo

Sempre use 4 espaços e nunca misture tabulações e espaços.

Se uma linha for continuada, existem duas opções aceitáveis:

``` python
# Correto
# opção 1, recue o parêntese de abertura:
foo = function_that_creates_bar(variável_1, variável2,
                           variável_3, variável_4)

# opção 2, adicione 4 espaços:
foo = function_that_creates_bar(
    variável_1, variável2,
    variável_3)
```

``` python
# Errado, em qualquer lugar.
foo = function_that_creates_bar(variável_1, variável2,
              variável_3)
```

### Tamanho máximo da linha

As linhas devem ser limitadas a um máximo de 79 caracteres.

### linhas em branco

- Separe as definições das classes e funções com duas linhas em branco.
- Os métodos dentro das classes são separados por uma linha em branco.
- Recomenda-se usar linhas em branco para separar partes do código, por exemplo, dentro de uma função, que executam tarefas diferentes.

### Importações

As importações de módulos diferentes devem estar em linhas diferentes:

``` python
# Sim:
import os
import sys
```

``` python
# Não:
import os, sys
```

Sim, os elementos que são importados do mesmo módulo podem ser colocados em uma linha:

``` python
from subprocess import Popen, PIPE
```

As importações devem ser sempre colocadas no início do arquivo, logo após os comentários e documentação do arquivo, e antes da definição das variáveis ​​e constantes globais.

As importações devem ser agrupadas na seguinte ordem:

1. bibliotecas ou módulos padrão.
2. bibliotecas ou módulos de terceiros.
3. bibliotecas ou módulos locais ou proprietários.

Cada grupo de importações deve ser separado por uma linha em branco.

### Espaços em branco em expressões

Evite espaço em branco extra em:

Dentro de parênteses, colchetes ou chaves.

``` python
# Sim:
spam(ham[1], {ovos: 2})
```

``` python
# Não:
spam(presunto[ 1 ], { ovos: 2 })
```

Antes de uma vírgula.

``` python
# Sim:
if x == 4: print x, y; x, y = y, x
```

``` python
# Não:
if x == 4: print x, y; x, y = y, x
```

Antes dos parênteses de uma chamada de função.

``` python
# Sim:
spam(1)
```

``` python
# Não, esse espaço é horrível
spam (1)
```

Antes do colchete de um índice ou chave.

``` python
# Sim:
dict['chave'] = lista[index]
```

``` python
# Não, esse espaço é tão assustador quanto o anterior
dict ['chave'] = lista [index]
```

Sempre separe os operadores binários com um único espaço em ambos os lados: atribuição (=), atribuição aumentada (+=, -= , etc.), comparação (==, <, >, !=, <>, <=, > = , in, not in, is, is not), booleanos (and, or, not).

Use espaços em torno de operadores aritméticos:

``` python
# Sim:
e = e + 1
enviado += 1
x = x * 2 - 1
hipot2 = x * x + y * y
c = (a + b) * (a - b)
```

``` python
# Não:
i=i+1
enviado +=1
x = x*2 - 1 #não recomendado, mas às vezes usamos
hipot2 = x*x + y*y
c = (a+b) * (a-b)
```

### Convenções de nomenclatura

As convenções de nomenclatura em Python são uma bagunça e provavelmente nunca teremos tudo consistente. No entanto, damos a você algumas das recomendações atuais sobre nomes. Novos módulos devem ser escritos respeitando-os, embora a consistência interna seja preferível para bibliotecas que já possuem partes feitas...

### Estilos de nomenclatura

Existem muitos estilos para nomear variáveis, funções, etc. É útil reconhecer qual estilo está sendo usado, independentemente de para que está sendo usado.

Aqui estão alguns estilos:

* b (letra simples, minúscula)
* B (letra simples, maiúscula)
* minúsculas
* minúsculas_com_sublinhados
* LETRAS MAIÚSCULAS
* MAIÚSCULAS_WITH_UNDERSCARDS
* Maiúsculas (também chamado de estilo camelo por causa das corcovas)
* mixedCase (diferente do camel na inicial)
* With_Caps_And_Underscores (horrível!)

**Recomenda-se** não usar acentos ou caracteres especiais de qualquer tipo para evitar problemas de compatibilidade. Os nomes de funções e variáveis ​​devem ser escritos em letras minúsculas, eventualmente usando sublinhados para melhorar a legibilidade.

### Há muito mais!

Este é apenas um breve resumo, veja [PEP 8](https://www.python.org/dev/peps/pep-0008/) para todas as informações sobre estilos recomendados em Python.

## Zen do Python

Já que estamos falando de PEPs, queremos mencionar o PEP 20 (PEP significa Python Enhancement Proposals), também conhecido como [Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python)

O Zen of Python é uma coleção de princípios de software que influenciam o design da linguagem. O texto, que copiamos abaixo, pode ser encontrado no site oficial do Python e também é incluído como surpresa no interpretador do Python ao escrever a instrução `import this`.

**Zen de Python**

>Bonito é melhor do que feio.\
>Explícito é melhor que implícito.\
> Simples é melhor que complexo.\
>Complexo é melhor que complicado.\
>Flat é melhor do que aninhado.\
>O espaçamento é melhor do que denso.\
>A legibilidade é importante.\
>Casos especiais não são especiais o suficiente para quebrar as regras.\
>No entanto, a praticidade supera a pureza.\
>Os erros nunca devem passar silenciosamente.\
>A menos que estejam explicitamente silenciados.\
>Em face da ambiguidade, evite a tentação de adivinhar.\
>Deve haver uma, e de preferência apenas uma, maneira óbvia de fazer isso.\
>Embora esse caminho não seja óbvio, a menos que você seja holandês.\
>Agora está melhor do que nunca.\
>Embora nunca seja muitas vezes melhor do que *agora*.\
>Se a implementação for difícil de explicar, é uma má ideia.\
>Se a implementação for fácil de explicar, pode ser uma boa ideia.\
>Os namespaces são uma ótima ideia, vamos fazer mais deles!

## Retono ao [sumario](./00_Resumo.md)