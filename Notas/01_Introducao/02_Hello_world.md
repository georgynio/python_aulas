# Olá mundo!

Como é tradicional, toda vez que vamos aprender uma linguagem de programação nova, devemos dar o `Olá mundo!` para não ter problemas no nosso aprendizado.

Daqui em diante o **interpretador do Python** será o nosso amigo mais valioso. Neste iremos fazer todo tipo de testes, desde partes de código, blocos, até um programa completo.

```bash
:~$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

## Modo iterativo

Ao executar `python3` estamos entrando no modo  *iterativo* e desde o começo podemos fazer testes.

Por exemplo, podemos fazer o primeiro teste de como deveria ser o nosso `Olá mundo!`.

```python
>>> print('Olá Mundo!')
Olá Mundo!
>>> print('Hello World')
Hello World
>>>
```

**Essa forma de escrever o código (no terminal) que é imediatamente avaliada e imprime o resultado, é chamada de Read-Eval-Print-Loop (REPL).**

Vejamos com maior detalhamento o funcionamento do REPL:

- `>>>` esse símbolo indica que o interpretador está disponível para trabalhar, caso ele não apareça significa que tem algum processo sendo executado.

- `...` indica que o interpretador está esperando a continuação da escrita do seu código.

Vamos testar o **underline** que vimos anteriormente `_` (guarda o último resultado).

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

Estes programas podem ser criados a partir de editores de texto tipo: `gedit`, `bloco de notas`, `notepad`, etc. Contudo, podemos encontrar ambientes mais adequados, os chamados entornos de desenvolvimento integrados (IDE por «Integrated Development Environment»), que são compostos por ferramentas que ajudarão na hora de programar. A exemplo: spyder, vscode, pycharm, etc.

### Execução de programas

Este processo é bastante simples, precisamos apenas do terminal aberto. Neste, devemos acessar a pasta onde o nosso script se encontra salvo. Para executar precisamos apenas de escrever `python` e o nome do script. Por exemplo:

No terminal linux:

```bash
bash$ python hello.py
hello world
bash$
```

Ou em um terminal do Windows:

```bash
C:\SomeFolder>hello.py
hello world

C:\SomeFolder>c:\python36\python hello.py
hello world
```

**Nota:** No Windows as vezes é preciso indicar o caminho do executável do Python, por exemplo:  `c:\python36\python`.

Normalmente aparecem erros na primeira vez da execução do script. Para tratar o erro podemos utilizar a opção `-i`, esta ação nos fará permanecer no interpretador do Python, por exemplo, `python -i hello.py`. Essa opção é boa quando temos problemas com codigos que realizam cálculos em várias etapas e precisamos testar algumas coisas.

### Nosso primeiro exemplo de programa

Vamos resolver o seguinte problema:

> Conta a lenda que o xadrez foi inventado na Índia, há mais de 1500 anos. O rei daquela época ficou tão fascinado com a invenção e as infinitas variações de movimentos, que resolveu recompensar o inventor.
>> Rei: O que você quer de recompensa?\
>> Inventor: Quero um grão de arroz para a primeira casa, dois grãos para a segunda casa, 4 para a terceira, e assim sucessivamente.\
>>Rei: “Só isso?”, o rei retrucou. \
Então, o rei pediu para os matemáticos do reino fazerem as contas.

Vamos ver qual seria a solução, **indo apenas até o oitavo quadrado**, pois a solução é gigante.

```python
# xadrez.py
quadros_tabuleiro = 8  # numero de quadros no tabuleiro
grao = 1        # primeiro grão de arroz
posicao = 1

print(posicao, grao, posicao-1)

while posicao <= quadros_tabuleiro:
    
    grao = grao * 2
    posicao = posicao + 1
    print(posicao, grao, posicao-1)

print('Quantidade de grãos', grao)
print('Equivale a elevar 2 à', posicao-1)
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

### Comentários

Os comentarios formam parte do programa, iniciam com `#` e automaticamente se comenta a linha completa. Esta ferramenta ajuda a entender o funcionamento do código, pois ele pode ter uma explicação completa da funcionalidade das linhas que vem depois.

> **Os acentos são aceitos apenas nos comentários**

```python
# Isto é um comentário
a = 3 + 4

# Cálculo do quadrado
b = a * 2
print(b)
```

**Nota:** Os comentários servem apenas para orientar ao programador ou para quem está lendo o código `não se executa`.

### Variável

É um objeto (nome) capaz de representar e reter um valor ou expressão. Estes nomes podem ter a estrutura que o programador desejar, tendo apenas a restrição de não começar por um número, usar carácter alfanuméricos ou espaços em branco.

```python
estatura = 1.80   # válido
_estatura = 1.80  # válido
estatura_2 = 1.80 # válido
2estatura = 1.80  # inválido
```

### Palavras reservadas

São palavras que o interpretador busca e usa para receber instruções.

> É possível utlizá-las como variável, porém, geralmente ocasiona erros quando usadas dessa maneira.

```bash
and         as          assert      break
class       continue    def         del
elif        else        except      False
finally     for         from        global
if          import      in          is
lambda      None        nonlocal    not
or          pass        raise       return
True        try         while       with
yield
```

***Nota:*** Tenha cuidado com o uso do underscore (`_`)  pois ele é comumente utilizado por programadores internacionais (com diferentes fins).

### Tipos

O tipo das variaveis não são definidos explicitamente e mudam dinamicamente de acordo com o valor asignado.

```python
altura = 442           # Inteiro
altura = 442.0         # Ponto flutuante
altura = 'Muy, muy alto' # Cadeia de caracteres
```

**Tipagem dinâmica:** que significa que o próprio Python infere o tipo de variável sem a necessidade da indicação do usuário e pode mudar durante a execução do programa.

### Python distingue entre maiusculas e minusculas

Característica do Python que pode ajudar na hora de enfatizar em alguma caracaterística de alguma variável.

```python
nome = 'David'
Nome = 'Diego'
NOME = 'Rosita'
```

Contudo, os comandos sempre se escrevem em letras minúsculas.

```python
while x < 0:   # OK
WHILE x < 0:   # ERROR
```

### Estrtuturas de repetição

Repetem uma série de instruções até atingir um limite estabelecido.

No caso do comando `while` executa o ciclo até uma que uma condição seja atingida. Normalmente a condição para quando se atinge a condição `true`.
> Se a condição não for definida adequadamente o comando roda infinitamente.

```python
while posisao <= quadros_tabuleiro:
    
    grao = grao * 2
    posisao = posisao + 1
    print(posisao, grao, posisao-1)

```

No caso do comando `for` as instruções serão repetidos uma quantidade de vezes previamente definidas pelo programador.

```python
for i in range(quadros_tabuleiro):
    grao = grao * 2
    print(i+1, grao, i)

```

### Identação

Uma caracteristica a destacar no python é o cuidado especial com a identação. Pois, com ela definimos partes do código que serão executados separadamente.

```python
while posisao <= quadros_tabuleiro:
    
    grao = grao * 2
    posisao = posisao + 1
    print(posisao, grao, posisao-1)

print('No exemplo esta porção se executa após a finalização do trecho anterior')
```

### Regras de identação

Devemos lembrar de seguir o seguinte:

- Utiliza-se espaço em branco e não o `tab`.
- Cada nível deve ter 4 espaços (recomendação geral).

As partes do código que tenham identação diferente serão executados como partes de outro trecho. Por exemplo, o código em seguida retornará erro ao ser executado:

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

Se colocar um `string` e uma `variável` na função `print`, ele coloca automaticamente o espaço em branco antes de imprimir o valor da variável.

```python
valor = 'poder'
print('Eu tenho o', valor) # faça o teste e veja o que acontece
```

Cada `print()` se executa de forma independente, quando temos um embaixo de outro este da salto de linha automaticamente.

```python
print('Hola')
print('Mi nombre es', 'Juana')
```

Deveria imprimir:

```code
Hola
Mi nombre es Juana
```

Esse salto pode ser suprimido utilizando a opção `end`.

```python
print('Hola', end=' ')
print('Mi nombre es', 'Juana')
```

Ele vai imprimir:

```code
Hola Mi nombre es Juana
```

### Comandos interessantes:

&check; `input()` lê o valor escrito pelo usuário no terminal.\
&check; `pass` indica que quando o execução do programa chega nesta parte, e ele deve pular para o próximo trecho do código, sem fazer nada.\
&check; `round` arredonda o valor de um decimal.\
&check; `pow` calcula a potência de um número.\
&check; `type` retorna uma mensagem com o tipo da variável.\
&check; etc.

## Retorno ao [sumário](./00_Resumo.md)