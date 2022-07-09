# Olá mundo!

Como é tradicional, toda vez que vamos aprender uma linguagem de programação nova, devemos dar o `Olá mundo!` para não ter problemas no nosso aprendizado.

Daqui em diante o **interprete do Python** será o nosso amigo mais valioso. Neste iremos fazer todo tipo de testes, podemos de partes de codigo, blocos e ainda o todo.

```bash
:~$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

## Modo iterativo

Ao executar `python3` estamos entrando ao modo  *iterativo* e desde o começo podemos fazer testes.

Por exemplo, podemos fazer o primeiro teste de como deveria ser o nosso `Olá mundo!`.

```python
>>> print('Olá Mundo!')
Olá Mundo!
>>> print('Hello World')
Hello World
>>>
```

Esta forma de escribir código (en una consola del lenguaje) que se evalúa inmediatamente e imprime el resultado, se denomina *bucle de Lectura-Evaluación-Impresión* (REPL por las siglas en inglés de «Read-Eval-Print-Loop»). Asegurate de poder interactuar con el intérprete antes de seguir.

Veamos en mayor detalle cómo funciona este REPL:

- `>>>` esse simbolo indica que o interprete esta disponivel para trabalhar, caso ele não apareça significa que tem algum processo sendo executado.

- `...` indica que o interprete esta esperando a continuação da escrita do seu codigo.

Vamos testar o  underline que vimos antes `_` (guarda o último resultado).

```python
>>> 37 * 42
1554
>>> _ * 2
3108
>>> _ + 50
3158
>>>
```

**Nota:** É valido apenas no modo iterativo.

### Criação de programas

Os programas devem ser salvos com a extensão `.py`, quem utiliza o `jupyter` a extensão será `.ipynb`.

```python
# hello.py
print('hello world')
```

Estes programas podem ser criados a partir de editores de texto tipo: `gedit`, `bloco de notas`, `notepad`, etc. Contudo, podemos encontrar ambientes mais adequados, entornos de desenvolvimento integrados (IDE por «Integrated Development Environment»), que são compostos por ferramentas que ajudarão na hora de programar.


### Execução de programas

Este processo é bastante simples, precisamos apenas o terminal aberto. Nesta, devemos nos localizar na pasta onde o nosso script se encontra salvo. Para executar precisamos apenas de escrever `python` e o nome do script. Por exemplo:

No terminal linux:

```bash
bash$ python hello.py
hello world
bash$
```

Ou numa terminal do Windows:

```bash
C:\SomeFolder>hello.py
hello world

C:\SomeFolder>c:\python36\python hello.py
hello world
```

**Nota:** No Windows as veces é preciso indicar o caminho do executavel do Python, por exemplo:  `c:\python36\python`.

Normalmente aparecem erros na primeira vez da execução do script. Para isto podemos usar a opção `-i` para permanecer no interprete do Python, por exemplo, `python -i hello.py`. Essa opção é boa quando temos problemas com codigos que realizam calculos em varias etapas e precisamos testar algumas coisas.


### Nosso primeiro exemplo de programa

Vamos resolver o seguinte problema:

> Conta a lenda que o xadrez foi inventado na Índia, há mais de 1500 anos. O rei daquela época ficou tão fascinado com a invenção e as infinitas variações de movimentos, que resolveu recompensar o inventor.
>> Rei: O que você quer de recompensa?\
>> Inventor: Quero um grão de arroz para a primeira casa, dois grãos para a segunda casa, 4 para a terceira, e assim sucessivamente.\
>>Rei: “Só isso?”, o rei retrucou. \
Então, o rei pediu para os matemáticos do reino fazerem as contas.

Vamos ver qual seria a solução, indo apenas até o quadro 8:

```python
# xadrez.py
quadros_tabuleiro = 8  # numero de quadros no tabuleiro
grao = 1        # primeiro grão de arroz
posisao = 1

print(posisao, grao, posisao-1)

while posisao <= quadros_tabuleiro:
    
    grao = grao * 2
    posisao = posisao + 1
    print(posisao, grao, posisao-1)

print('Quantidade de grãos', grao)
print('Equivale a elevar 2 à', posisao-1)
```

Ao executar o programa obtemos:

```bash
bash$ python3 xadrez.py
1 1 0
2 2 1
3 4 2
4 8 3
5 16 4
6 32 5
7 64 6
8 128 7
9 256 8
Quantidade de grãos 256
Equivale a elevar 2 à 8
```



### Comandos

Um programa de Python é um conjunto de instruções (comandos) que descrevem uma tarefa que o computador deve realizar:

```python
a = 3 + 4
b = a * 2
print(b)
```


### Comentarios

Os comentarios formam parte do programa, iniciam com `#` e automaticamente se comenta a linha completa. Esta ferramenta ajuda a entender o funcionamento do codigo, pois ele pode ter uma explicação completa da funcionalidade das linhas que vem depois.

```python
# Esto es un comentario
a = 3 + 4

# Calculo do quadrado
b = a * 2
print(b)
```

**Nota:** Os comentarios servem apenas para orientar ao programador ou para quem esta lendo o codigo `não se executa`.

### Variável

É um objeto (nome) capaz de representar e reter um valor ou expressão. Estes nomes podem ter a estrutura que o programador desejar, tendo apenas a restrição de não começar por um numero, usar carater alfanumericos ou espaços em branco. 

```python
estatura = 1.80   # valido
_estatura = 1.80  # valido
estatura_2 = 1.80 # valido
2estatura = 1.80  # não valido
```

### Palavras reservadas

São palavras que o interpretador busca e usa para receber instruções. Ao todo são 31 palavras reservadas na sintaxe:

```bash
and del from not while
as elif global or with
assert else if pass yield
break except import print
class exec in raise
continue finally is return
def for lambda try
```

### Tipos

O tipo das variaveis não são definidos explicitamente e mudam dinamicamente de acordo com o valor asignado.

```python
altura = 442           # Entero
altura = 442.0         # Punto flotante
altura = 'Muy, muy alto' # Cadena de caracteres
```

**Tipado dinâmico:** que significa que o proprio Python infere o tipo de variavel sem a necessidade da indicação do usuario e pode mudar durante a execução do programa.


### Python distingue entre maiusculas e minusculas

Caracteristica do Python que pode ajudar na hora de enfatizar em alguma caracateristica de alguma variável. 

```python
nombre = 'David'
Nombre = 'Diego'
NOMBRE = 'Rosita'
```

Contudo, os comando sempre se escrevem em minuscula.

```python
while x < 0:   # OK
WHILE x < 0:   # ERROR
```

### Estrtuturas de repetição

Repetem uma serie de instruções até atingir um limite estabelecido.

No caso do comando `while` executa o ciclo até uma que uma condição seja atingida. Normalmente a condição para quando se atinge a condição `true`. 
> Se a condição não é definida adequadamente o comando roda infinitamente.

```python
while posisao <= quadros_tabuleiro:
    
    grao = grao * 2
    posisao = posisao + 1
    print(posisao, grao, posisao-1)

```

No caso do comando `for` as instruções serão repetidos uma quantidade de veces previamente definidos pelo programador.

```python
for i in range(quadros_tabuleiro):
    grao = grao * 2
    print(i+1, grao, i)

```

### Identação

Uma caracteristica a destacar do python é o especial cuidado com a identação. Pois, com ela definimos partes do codigo que serão executados por separado. 

```python
while posisao <= quadros_tabuleiro:
    
    grao = grao * 2
    posisao = posisao + 1
    print(posisao, grao, posisao-1)

print('No exemplo esta porção se executa após a finalização do trecho anterior')
```

### Regras de identação

Devemos lembrar de seguir o seguinte:

* Usa espaço em branco não o `tab`.
* Cada nivel deve ter 4 espaços (recomendação geral).

As partes do codigo que tenham identação diferente serão executados como partes de outro trecho. Por exemplo, o trecho de codigo em seguida retorna erro ao ser executado:

```python
while posisao <= quadros_tabuleiro:
    
    grao = grao * 2
      posisao = posisao + 1
    print(posisao, grao, posisao-1)

```

### Condicional

As condições são avaliadas utilizando o comando `if` e `else`:

```python
if a > b:
    print('O maior é a')
else:
    print('O maior é b')
```

Podemos agregar condições extras utilizando `elif`.

```python
if a > b:
    print('O maior é a')
elif a == b:
    print('São iguais!')
else:
    print('O maior é b')
```


### Impressão em tela

O comando que nos ajuda neste quesito é o `prirnt`, que retorna em tela uma mensagem com os argumentos indicados.

```python
print('Hello world!') # Imprime 'Hello world!'
```

Podemos imprimir variáveis.

```python
x = 100
print(x) # imprime o valor de 'x'
```

Se coloca um string e uma variavel, ele coloca automaticamente o espaço em branco antes de imprimir o valor da variável.

```python
valor = 'poder'
print('Eu tenho o', valor) # faça o teste e veja o que acontece
```

cada `print()` se executa de forma independente, quando temos um embaixo de outro este da salto de linha automaticamente.

```python
print('Hola')
print('Mi nombre es', 'Juana')
```

Deveria imprimir:

```code
Hola
Mi nombre es Juana
```

Esse salto pode ser suprimido.

```python
print('Hola', end=' ')
print('Mi nombre es', 'Juana')
```

E deveria imprimir:

```code
Hola Mi nombre es Juana
```

### Comandos interessantes:

&check; `input()` lê o valor ingressado pelo usuario desde o terminal.\
&check; `pass` indica que quando o execução do programa chega nesta parte ele deve pular para o proximo trecho do codigo, sem fazer nada.\
&check; `round` arredonda o valor de um decimal.\
&check; `pow` calcula a potencia de um numero.\
&check; `type` retorna uma mensagem com o tipo da variavel.\
&check; etc.

## Retono ao [sumario](/Notas/01_Introducao/00_Resumo.md)