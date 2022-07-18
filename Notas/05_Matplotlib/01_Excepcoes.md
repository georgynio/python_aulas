# Controle de erros

Embora já tenhamos falado de forma breve sobre *exceções*, nesta seção falaremos sobre tratamento de exceções e erros com mais detalhes.

## Como os programas falham

O Python não faz nenhuma verificação ou validação sobre os tipos de argumentos que as funções recebem ou os valores desses argumentos. As funções funcionarão em qualquer situação que seja possivel realizar a tarefa indicada.

``` python
def add(x, y):

    return x + y

add(3, 4) # 7
add('Olá', 'mundo') # 'Olá mundo'
add('3', '4') # '34'
```

Se houver erros em uma função, eles serão mostrados apenas quando forem executados.

``` python
def add(x, y):
    retornar x + y

>>> add(3, '4')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +::
'int' and 'str'
>>>
```

Python retorna a mensagem dos erros em inglês. O erro mostrado acima pode ser traduzido como:

```bash
Recapitulando (chamada mais recente no final)
...
Erro de tipo (dados): tipo de argumento não suportado para +: 'int' e 'str'.
```

Ou seja: a função tentou aplicar o operador + (adição) a dois argumentos de tipos diferentes (integer e string) e não conseguiu. Por isso ele abriu uma exceção.

## Exceções

Como já dissemos, as exceções são uma forma de sinalizar erros em tempo de execução. Lembre-se que você pode lançar uma exceção usando o comando `raise`.

``` python
if  nome not in autorizados:
    raise RuntimeError(f'{nome} não autorizado')
```

Para *capturar* uma exceção, use um bloco `try-except`.

``` python
try:
    autenticate(usuario)
except RuntimeError as e:
    print(e)
```

## Manipulação de exceção

Uma exceção será propagada para o primeiro `except` que corresponder a ela.

``` python
def grok():
    ...
    raise RuntimeError('Epa!') # Cria uma exceção aqui

def spam():
    grok() # Esta chamada irá gerar uma exceção

def bar ():
    try:
        Spam()
    except RuntimeError as e: # Aqui pegamos a exceção
        ...

def foo():
    try:
        bar()
    except RuntimeError as e: # Portanto a exceção não chega aqui
        ...

foo()
```

Para lidar com a exceção, use instruções no bloco `except`. Qualquer instrução fará com que o Python trate a exceção como tratada, até mesmo um `pass`, mas é pertinente executar ações relacionadas à exceção específica a ser tratada.

``` python
def grok(): ...
    raise RuntimeError('Ei!')

def barr():
    try:
      grok()
    except RuntimeError as e: # Exceção capturada
        instrucoes # Executa estes comandos
        instrucoes
        ...

bar()
```

Uma vez que a exceção é capturada, a execução continua na primeira instrução após o `try-except`.

``` python
def grok(): ...
    raise RuntimeError('Ei!')

def barr():
    try:
      grok()
    except RuntimeError as e: # Exceção capturada
        instrucoes
        instrucoes
        ...
    instrucoes # A execução do programa
    instrucoes # continue aqui
    ...

bar()
```

## Exceções incorporadas

Existem mais de vinte tipos de exceções já incorporadas ao Python. Normalmente, o nome da exceção indica o que deu errado (por exemplo, um `ValueError` é gerado se o valor fornecido não for adequado). A continuação podemos ver alguns erros comun, o restando pode ser encontrado na [documentação](https://docs.python.org/pt-br/3/library/exceptions.html#bltin-exceptions).

``` python
ArithmeticError
AssertionError
EnvironmentError
EOFError
ImportError
IndexError
KeyboardInterrupt
KeyError
MemoryError
NameError
ReferenceError
RuntimeError
SyntaxError
SystemError
TypeError
ValueError
```

## Valores associados a exceções

As exceções geralmente têm valores associados, que fornecem mais informações sobre a causa exata do erro. Esse valor pode ser uma string (*string*) ou uma tupla com valores diferentes (por exemplo, um código de erro e um texto explicando esse código).

``` python
raise RuntimeError('Nome de usuário inválido')
```

A instância da variável fornecida a `except` (nos nossos exemplos `e`) tem este valor associado a ela.

``` python
try:
    ...
except RuntimeError as e:
    # `e` contém a exceção lançada com sua mensagem específica
    ...
```

`e` é uma instância do mesmo tipo que a exceção, embora se você imprimi-la, geralmente se parece com uma string.

``` python
except RuntimeError as e:
    print('Falha. Motivo:', e)
```

## Você pode capturar várias exceções

É possível capturar diferentes tipos de exceções no mesmo trecho de código, se você incluir vários `except` em seu `try:`.

``` python
try:
  ...
except LookupError as e:
  ...
except RuntimeError as e:
  ...
except IOError as e:
  ...
except KeyboardInterrupt as e:
  ...
```

Como alternativa, se você for processá-los da mesma maneira, poderá agrupá-los:

``` python
try:
  ...
except (IOError, LookupError, RuntimeError) as e:
  ...
```

## Todas as exceções

Para capturar todas e quaisquer exceções, use `Exception` assim:

``` python
try:
    ...
except Exception: # PERIGO. (ver abaixo)
    print('Ocorreu um erro')
```

Geralmente, é uma má ideia "tratar" exceções dessa maneira, porque isso não fornece nenhuma pista do motivo pelo qual o programa falhou. Você só sabe que "Houve um erro".

## Portanto, NENHUMA exceção é capturada.

É assim que o tratamento de exceções NÃO deve ser feito.

``` python
try:
    fazer algo()
except Excetion:
    print('Ocorreu um erro.')
```

Isso captura todos os erros possíveis e pode dificultar muito a depuração quando seu código falha por algum motivo que você não esperava (por exemplo, algum módulo Python está ausente e tudo o que informa é "Ocorreu um erro").

## Isso é um pouco melhor.

Se você vai pegar todas as exceções, aqui está uma maneira um pouco mais decente:

``` python
try:
    fazer algo()
except Exception as e:
    print('Ocorreu um erro. Porque...', e)
```

`Exception` inclui todas as exceções possíveis, então você não sabe qual delas você capturou.
Pelo menos esta versão informa o motivo específico do erro. É sempre bom ter alguma maneira de visualizar ou relatar erros quando você captura todas as exceções possíveis.

No entanto, geralmente é melhor detectar bugs específicos e apenas aqueles que você pode gerenciar. Erros que você não sabe como lidar corretamente, deixe-os rodar (talvez algum outro pedaço de código os capture e os trate corretamente, ou talvez seja melhor parar a execução).

## Relançar uma exceção

Se você precisa fazer algo em resposta a uma exceção, mas não quer pegá-la, você pode usar `raise` para relançar a mesma exceção.

``` python
try:
    fazer algo()
except Exception as e:
    print('Ocorreu um erro. Porque...', e)
    raise
```

Isso permite que você, por exemplo, acompanhe as exceções (*log*) sem manipulá-las e relançá-las para tratá-las adequadamente mais tarde.

## Práticas recomendadas ao lidar com exceções

Não capture exceções que você não tratará corretamente. Solte-os ruidosamente. Se for importante, alguém cuidará do problema. Apenas pegue exceções se *você for esse "alguém"*. Ou seja: pegue apenas aqueles erros que você pode gerenciar elegantemente de uma forma que permita que o programa continue rodando.

## A declaração `finally`

`finally` especifica que esse pedaço de código deve ser executado independentemente de uma exceção ter sido capturada ou não.

``` python
lock = Lock()
...
lock.acquire()
try:
    ...
finally:
    lock.release() # isso é SEMPRE executado. Se há ou não exceções.
```

Uma estrutura como essa resulta em um gerenciamento seguro dos recursos disponíveis (seguros, arquivos, hardware, etc.)

## Retorno ao [sumário](./00_Resumo.md)