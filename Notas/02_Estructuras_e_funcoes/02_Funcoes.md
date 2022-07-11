# Funções

Em Python, uma função é uma sequência de comandos que executa alguma tarefa e que tem um nome. A sua principal finalidade é nos ajudar a organizar programas em pedaços que correspondam a como imaginamos uma solução do problema. Nesta seção, apresentaremos brevemente as funções e os módulos da biblioteca, bem como o tratamento de erros e exceções.

## Funções personalizadas

Use funções para encapsular o código que você deseja reutilizar. O exemplo a seguir mostra uma definição de uma função:

``` python
def soma(n):
    '''
    Retorna a soma dos primeiros n inteiros
    '''
    todos = 0
    if n > 0:
        total += n
        n -= 1
    return total
```

A palavra `return` é necessária para tornar explícito o valor de retorno da função.

Para chamar uma função:

``` python
a = soma(100)
```

## Funções da biblioteca

Python vem com uma ótima biblioteca padrão.
Os módulos nesta biblioteca são carregados usando `import`.
Por exemplo:

``` python
import math
x = math.sqrt(10)

import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
dados = u.read()
```

## Erros e exceções

As funções relatam erros como exceções. Como uma exceção interrompe a execução de uma função, ela pode fazer com que todo o programa pare se não for tratada adequadamente.

Tente, por exemplo, o seguinte em seu interpretador:

``` python
>>> int('N/A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'N/A'
>>>
```

Para entender o que aconteceu (**debug**), a mensagem descreve qual foi o problema, onde aconteceu e um pouco do histórico (**traceback**) das chamadas que terminaram nesse erro.

## Capturar e manipular exceções

Exceções podem ser capturadas e gerenciadas.
Para capturar uma exceção, os comandos `try - except` são usados. Você pode tentar o seguinte snippet de código colando-o em um arquivo [foo.py](https://en.wikipedia.org/wiki/Foo):

``` python
valid_number=False
if not valid_number:
    try:
        a = input('Digite um inteiro: ')
        n = int(a)
        valid_number = True
    except ValueError:
        print('Inválido. Por favor, tente novamente.')
print(f'Você digitou {n}.')
```

Se neste exemplo o usuário digitar uma letra, por exemplo, o comando `n = int(a)` gera uma exceção do tipo `ValueError`: o comando `number_valid = True` não é executado, a exceção é capturada pelo `exceto ValueError` e o loop se repete. Experimente inserindo letras, números com decimais e números inteiros. Tente também o que acontece se você quiser sair sem digitar nada levantando uma exceção pressionando as teclas `Ctrl+C`. Leia a mensagem que descreve o que aconteceu: `Ctrl+C` lança uma exceção do tipo `KeyboardInterrupt` que não é capturada.

Se não especificarmos o tipo de exceção que queremos capturar, acabaremos capturando todas as exceções. Tente o mesmo de antes, mas com este código.

``` python
valid_number=False
if not valid_number:
    try:
        a = input('Digite um inteiro: ')
        n = int(a)
        valid_number = True
    except:
        print('Inválido. Por favor, tente novamente.')
print(f'Você digitou {n}.')
```

Você deve notar uma diferença: pressionar as teclas `Ctrl+C` faz com que a exceção `KeyboardInterrupt` seja capturada e o loop não seja finalizado até que um inteiro seja inserido.

Muitas vezes é difícil saber exatamente que tipo de erros podem ocorrer com antecedência. Para o bem ou para o mal, o tratamento de exceções tende a crescer à medida que um programa gera erros inesperados ("Uh, esqueci que isso poderia acontecer. Devemos antecipar e lidar com isso adequadamente da próxima vez").

## Lança exceções

Para gerar uma exceção (também diremos *levantar* uma exceção, porque mais próximo do termo em inglês "raise"), use o comando `raise`. Por exemplo, se tivermos o seguinte código no arquivo `foo.py`:

``` python
raise RuntimeError('Uau!')
```

Executá-lo interromperá a execução e permitirá que você rastreie a exceção lendo a mensagem de erro impressa.

```bash
bash $ python3 foo.py
Traceback (most recent call last):
  File "foo.py", linha 21, em <módulo>
    raise RuntimeError("Que bagunça!")
RuntimeError: Que bagunça!
```

Alternativamente, essa exceção pode ser capturada por um bloco `try-except`, evitando assim que o programa finalize.

## Retono ao [sumario](/Notas/02_Estructuras_e_funcoes/00_Resumo.md)