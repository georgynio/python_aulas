# Cadenas (strings)

São dados definidos entre aspas duplas (") ou simples ('), representado um texto, podendo conter letras, números, simbolos. Podemos encontrar a documentação no site [Operações comuns de strings](https://docs.python.org/pt-br/3/library/string.html).

## Representação de textos

O Python aceita diferentes formas de uso das aspas:

```python
# Aspas simples
a = 'A pressa é a inimiga da perfeição.'

# Aspas duplas
b = "A corda sempre arrebenta do lado mais fraco."

# Aspas triplas
c = '''
PEDRA NEGRA SOBRE PEDRA BRANCA (Cesar Vallejo)

Morrerei em Paris com aguaceiros
num dia de que já tenho a lembrança.
Morrerei em Paris - daqui não saio -
numa quinta-feira, como hoje, de outono.

Quinta-feira será, pois hoje, quinta-feira,
em que estes versos proso, dei os úmeros
à pouca sorte, e nunca como hoje
voltei,com todo o meu caminho, a ver-me só.

Morreu César Vallejo, espancavam-no
todos sem que lhes fizesse nada;
davam-lhe forte com um pau e forte

com uma corda também; são testemunhos
as quintas-feiras e os ossos úmeros,
a solidão, os caminhos, a chuva...
'''
```

Normalmente as cadeias de caracterese ocupam apenas uma linha. Pelo que a aspas triplas deixam escrever varias linhas.

Não há diferença entre aspas aspas simples (') e aspas duplas ("). Porém, ao fechar devemos usar o mesmo que usamos ao abrir. Se quisermos usar aspas dentro de uma string de aspas normal,caso sejam diferentes podem ser usados normalmente. Caso contrario, podemos usar `\`.
por exemplo:

```python
a = "Aspas simples 'dentro de aspas duplas'"
b = 'Aspas simples 'dentro de aspas simples''   # errado
b = 'Aspas simples \'dentro de aspas simples\'' # correto
```

Confere o que acontece com as aspas duplas.

## Código de escape

Significa que iremos inserir caracteres que tenham um significado especial. Estes começam com uma barra invertida, `\`. Usualmente encontraremos os seguintes:

```bash
'\n'      Caracter ASCII Linefeed (LF) - este cria uma nova
linha no output
'\r'      Caracter ASCII Carriage Return (CR)
'\t'      Caracter ASCII Tab Horizontal (TAB)
'\''      Aspa simples
'\"'      Aspas duplas
'\\'      Contrabarra
```

*Utilisa o `print()` e confere o resultado de usar esses codigos*.

Se desejamos escrever multiplas linhas podemos usar a `\`.

```python

a = ('PEDRA NEGRA SOBRE PEDRA BRANCA (Cesar Vallejo) \n'\
    'Morrerei em Paris com aguaceiros\n'\
    'num dia de que já tenho a lembrança.\n'\
    'Morrerei em Paris - daqui não saio -\n'\
    'numa quinta-feira, como hoje, de outono.\n\n'\

    'Quinta-feira será, pois hoje, quinta-feira,\n'\
    'em que estes versos proso, dei os úmeros\n'\
    'à pouca sorte, e nunca como hoje\n'\
    'voltei,com todo o meu caminho, a ver-me só.\n\n'\

    'Morreu César Vallejo, espancavam-no\n'\
    'todos sem que lhes fizesse nada;\n'\
    'davam-lhe forte com um pau e forte\n\n'\

    'com uma corda também; são testemunhos\n'\
    'as quintas-feiras e os ossos úmeros,\n'\
    'a solidão, os caminhos, a chuva...\n')
```

*Avalia o resultado utilizando a função `print()`.

## Strings como listas

No Python as strings funcionan como os vetores en matemática, permitindo o acesso a cada carater. **O index começa desde o zero**. Os index negativos indicam que possicionamento começa desde o ultimo elemento.

```python
a = 'Hello world'
b = a[0]          # 'H'
c = a[4]          # 'o'
d = a[-1]         # 'd' (fim do string)
```

Podemo também usar *porções* (slice) especificando um range de index com `:`.

```python
d = a[:5]     # 'Hello'
e = a[6:]     # 'world'
f = a[3:8]    # 'lo wo'
g = a[-5:]    # 'world'
```

## Operações com strings

Concatenação, longitude, pertenência e replicação.

```python
# Concatenação (+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say ' + a          # 'Say HelloWorld'

# longitude (len)
s = 'Hello'
len(s)                  # 5

# Test de pertenência (in, not in)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# Replicação (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'
```

## Métodos das strings

As strings em Python tem *métodos* com as quais podemos realisar varias operaçãoes.

Exemplo: apaga (strip) os espaços em branco do inicio e final.

```python
s = '  Hello '
t = s.strip()     # 'Hello'
```

Exemplo: Trocar entre mayúsculas e minúsculas.

```python
s = 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'
```

Exemplo: Substituição de texto.

```python
s = 'Hello world'
t = s.replace('Hello' , 'Olá')   # 'Olá world'
```

**Mais métodos:**

```python
s.endswith(suffix)     # Confere se termina com o sufixo
s.find(t)              # Primeira ocorrência de t em s (ou -1 se não estiver presente)
s.index(t)             # Primeira ocorrência de t em s (erro se estiver faltando)
s.isalpha()            # Verifique se os caracteres são alfabéticos
s.isdigit()            # Verifique se os caracteres são numéricos
s.islower()            # Verifique se os caracteres são minúsculos
s.isupper()            # Verifique se os caracteres são maiúsculos
s.join(slist)          # Junte-se a uma lista de strings usando s como delimitador
s.lower()              # Muda para minúsculas
s.replace(old,new)     # Troca o texto
s.split([delim])       # Divide a strings em menores
s.startswith(prefix)   # Confere se inicia com um prefixo
s.strip()              # Apaga (strip) os espaços em branco do inicio e final
s.upper()              # Troca para mayúsculas
```

## Mutabilidad de strings

Os strings são inmutaveis, sendo apenas de leitura.
Uma vez criados, o seu valor não pode ser mudado.

```python
>>> s = 'Hello World'
>>> s[1] = 'a' # Tentando trocar o 'e' por uma 'a'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

*Devemos inferir que as operações que manipulam strings criam novas strings para salvar os resultados.*

## Conversão de strings

Nem todos os objetos fornecem uma representação que possa ser reproduzida; neste caso eles forncem uma string fechada por tags "<>". Como o exemplo do `type(c)`.

```python
>>> x = 42
>>> str(x)
'42'
>>> type(x)
>>> c = str(x) #verificando se realmente muda o inteiro para string
>>> type(c)
<class 'str'>
>>> "{0} {0!s} {0!r} {0!a}". format(decimal.Decimal('93.4'))
"93.4 93.4 Decimal('93.4') Decimal('93.4')"
>>> filme = 'ภาพยนตร์'
>>> "{0}!a".format(filme)
"'\\u0e20\\u0e32\\u0e1e\\u0e22\\u0e19\\u0e15\\u0e23\\u0e4c'"
```

* O `r` força uma forma representacional e `a` força uma forma representacional mas usando apenas caracteres ASCII.

## f-Strings

As f-Strings são strings em que algumas expressões podem ser formatadas:

```python
>>> nome = 'Laranja'
>>> caixas = 100
>>> preco = 91.1
>>> a = f'{nome:>10s} {caixas:10d} {preco:10.2f}'
>>> a
'   Laranja        100      91.10'
>>> b = f'Custo = ${caixas*preco:0.2f}'
>>> b
'Custo = $9110.00'
>>>
```

**Nota:** Esta função está ativa a partir do Python 3.6.

## Retono ao [sumario](./00_Resumo.md)