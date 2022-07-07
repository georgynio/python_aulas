# Erros

Até agora mensagens de erro foram apenas mencionadas, mas se você testou alungs exemplos, talvez tenha esbarrado em algumas. Existem pelo menos dois tipos distintos de erros: erros de sintaxe e exceções. Podemos encontrar um relatorio completo dos erros no site da [documentação](https://docs.python.org/pt-br/3/tutorial/errors.html).

## Três tipos de erros:

Programando podemos encontrar três tipos de erros.

Os *erros sintáticos* são aqueles que ocorrem quando escrevemos incorretamente. Por exemplo, se quisermos escrever `x = (a + b) * c` mas em vez disso escrever `x = (a + b] * c`, o programa não será executado.

```python 
>>> x = (a + b] * c
  File "<stdin>", line 1
    x = (a + b] * c
              ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
```

Um segundo tipo de erro são os erros de *tempo de execução*, que ocorrem quando o programa começa a ser executado, mas ocorre um erro durante a execução. Por exemplo, se pedirmos ao usuário para digitar sua idade esperando um número inteiro e ele digitar "vinte e seis anos", é provável que o programa dê um erro. Se lermos um arquivo CSV e uma linha tiver dados ausentes, o programa poderá dar um erro. Esses tipos de erros em Python geram _exceções_ que, como veremos mais adiante, podem ser tratadas adequadamente.

```python
>>> idade = int(input('Coloque sua idade: '))
Coloque sua idade: vinte
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'vinte'
```

O terceiro tipo de erro é o mais difícil de encontrar e entender. São os *erros de semântica*, que ocorrem quando o programa não faz o que foi projetado para fazer. Eles têm a ver com o significado das instruções. Nesses casos, o programa é executado, mas apresenta um resultado incorreto ou inesperado. Em geral, a melhor maneira de encontrar esses erros é percorrer o código que gera um resultado inesperado, tentando entender onde está o erro, usando o depurador.

Por exemplo, calcula x = (2+3)*5
```python
# solução correta
>>> x = (2+3)*5
>>> x
25

# esquecemos dos parenteces
>>> x = 2+3*5
>>> x
17

```


## Depurar manualmente

Erros (ou bugs) são difíceis de rastrear e resolver. Especialmente erros que só aparecem sob uma certa combinação de condições que fazem com que o programa não consiga continuar ou dê um resultado inesperado. Se o seu programa roda, mas não dá o resultado esperado, ou _trava_ e você não entende o porquê, você tem algumas ferramentas específicas que o ajudam a encontrar a origem do problema. 

### O que diz um traceback?

Se você receber um erro, a primeira coisa que você pode fazer é tentar entender a causa do erro usando o "traceback" como ponto de partida:

```bash
python3 blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", line 4, in spam
    x.append(3)
AttributeError: 'int' object has no attribute 'append'
```

A última linha diz algo como "o objeto `int` não possui um atributo `append` "- o que é óbvio, mas como chegamos lá?

A última linha é o motivo específico do erro.

As linhas acima informam o caminho que o programa percorreu para chegar ao erro. Neste caso: o erro ocorreu em `x.append(3)` na linha 4, dentro da função `spam` do módulo `"blah.py"`, que foi chamado pela função `bar` na linha 7 do mesmo arquivo, que foi chamado por... e assim por diante.

No entanto, às vezes isso não fornece informações suficientes (por exemplo, não sabemos o valor de cada parâmetro usado nas chamadas).

Uma possibilidade que às vezes funciona é copiar o rastreamento para o Google. Se o erro for muito comum encontraremos muitas alternativas de solução. Se recomenda o uso do site https://pt.stackoverflow.com/, de preferencia o site em ingles.

### Use o modo [REPL](https://en.wikipedia.org/wiki/REPL) do Python


Se você usa o Python na linha de comando, pode usá-lo passando um `-i` como parâmetro antes do script a ser executado. Quando o interpretador Python terminar de executar o script, ele permanecerá no modo interativo (em vez de retornar ao sistema operacional). Você pode descobrir em que estado o sistema estava.

```bash
python3 -i blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", line 4, in spam
    x.append(3)
AttributeError: 'int' object has no attribute 'append'
>>> print(repr(x))

```

Este *parâmetro* (o `-i`, que usamos antes) preserva o estado do interpretador no final do script e permite que você o questione sobre o estado das variáveis ​​e obtenha informações que, de outra forma, você perderia. No exemplo, queremos apenas saber o que é `x` e como ele chegou a esse estado. 

### Depurar com `print`

`print()` é uma maneira rápida e fácil de deixar o programa rodar (quase) normalmente enquanto fornece informações sobre o estado das variáveis. Se você escolher as variáveis ​​a serem exibidas com sabedoria, provavelmente dirá "Aha!".

*Dica: É conveniente usar `repr()` para imprimir as variáveis*

``` python
def spam(x):
    print('DEBUG:', repr(x))
    ...
```

`repr()` fornece uma representação tecnicamente mais precisa do valor de uma variável, e não a representação *bonita* que normalmente vemos.

``` python
>>> from decimal import Decimal
>>> x = Decimal('3.4')
# SEM `repr`
>>> print(x)
3.4
# COM `repr`
>>> print(repr(x))
Decimal('3,4')
>>>
```

### Depurar com lápis e papel

Muitas vezes a pessoa *supõe* que o intérprete está fazendo alguma coisa. Se você pegar um lápis e papel e _desempenhar o papel de intérprete_ anotando o estado de cada variável e seguindo as instruções do programa passo a passo, você pode entender que as coisas não são como você pensava.

Essas alternativas são úteis, mas um pouco primitivas. A melhor maneira de depurar um programa Python é usar o depurador.