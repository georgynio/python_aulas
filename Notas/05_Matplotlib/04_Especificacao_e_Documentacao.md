# Contratos: Especificação e Documentação

## Comentários vs documentação

**Comentarios** são desciptores que ajudam ao programador a entender melhor a intenção e funcionalidade do programa. Estes são completamente ignorados pelo interprete do Python.

**Documentação** são cadeias de strings usados depois da definição de uma função, metodo, classe ou modulo (é chamado de [docstring](https://peps.python.org/pep-0257/)). A *documentação* destina-se a explicar *o que* o código faz.

Podemos ver a diferença entre documentação e comentários no
função `choose_code`:

``` python
def escolha_codigo():
    '''Retorna um código de 4 dígitos escolhido aleatoriamente'''
    digitos = ('0','1','2','3','4','5','6','7','8','9')
    codigo = ""
    for i in range(4):
        candidato = random.choice(digits)
        # Devemos ter certeza de não repetir dígitos
        while candidato in codigo:
            candidato = random.choice(digits)
        codigo = codigo + candidato
    return codigo
```

A documentação pode ser consultado na linha de comando

```python
>>> help(escolha_codigo)
```

O que retorna, na tela do terminal.

```bash
Help on function escolha_codigo in module __main__:

escolha_codigo()
    Retorna um código de 4 dígitos escolhido aleatoriamente
(END)

```

Podemos também verificar a documentação com ajuda do `print`.

```python
>>> print(escolha_codigo.__doc__)
Retorna um código de 4 dígitos escolhido aleatoriamente
>>>
```

### Autodocumentação

Em teoria, se nosso código pudesse transmitir eficientemente todos esses
conceitos, a documentação seria menos necessária. De fato, existe uma técnica de programação chamada *código autodocumentado*, em que a ideia principal é escolher os nomes das funções e variáveis ​​de tal forma que a documentação seja menos essencial.

Vamos pegar o seguinte código como exemplo:

``` python
a = 9,81
b = 5
c = 0,5 * a * b**2
```

Lendo essas três linhas de código podemos raciocinar qual o valor final de as variáveis ​​`a`, `b` e `c`, mas não há nada para nos dizer o que elas representam essas variáveis, ou qual é a intenção do código. Uma opção para melhorá-lo seria usar comentários para esclarecer a intenção:

``` python
a = 9,81 # Valor da constante G (aceleração gravitacional), em m/s²
b = 5 # Tempo em segundos
c = 0,5 * a * b**2 # Deslocamento (em metros)
```

Outra opção, de acordo com a técnica de código autodocumentado, é simplesmente atribuir nomes descritivos para variáveis:

``` python
aceleracao_gravitacional = 9,81
tempo_segundos = 5
deslocamento_meters = 0,5 * aceleracao_gravitacional * tempo_segundos ** 2
```

Desta forma conseguimos que a intenção do código seja mais clara, e que a necessidade de comentários e documentação para compreendê-lo é reduzida.

A técnica de código de autodocumentação tem várias limitações. Entre elas:

- Requer levar em consideração coisas como: quão descritivo é o nome (quanto mais, melhor), o comprimento do identificador (não deve ser excessivamente longo),o escopo do identificador (quanto maior, mais descritivo o nome deve ser) e convenções (`i` para índices, `c` para caracteres, etc).
- Por mais que escolhamos bem os nomes, muitas vezes a única maneira de explicar a intenção do código e todos os seus detalhes é mediante a documentação.

### Um erro comum: excesso de documentação e comentarios

Embora a ausência de documentação seja muitas vezes prejudicial, o outro extremo assim é: a *sobredocumentação*. Por exemplo:

``` python
def find_element(list_of_numbers, numero):
    '''Esta função retorna o índice (contando de 0) no qual
       encontra o número `number` na lista `list_of_numbers`.
       Se o elemento não estiver na lista, ele retornará -1.
    '''
    # Percorremos todos os índices da lista, de 0 (inclusive) a N
    # (não incluído)
    for index in range(len(list_of_numbers)):
        # Se o elemento na posição `index` for o procurado
        if list_of_numbers[índice] == número:
            # Retornamos o índice em que o elemento está
            return index
    # Não encontramos, retornamos -1
    return -1
```

Algumas coisas que podemos melhorar no exemplo:

- Na assinatura da função os nomes `find_element`, `list_of_numbers` e `numero` podem ser simplificados para `index`, `sequence` e `element`. Mudamos `list_of_numbers` para `list`, pois a função pode receber sequências de qualquer tipo, com elementos de qualquer tipo, e não há razão para limitá-la a ser uma lista de números.
- A variável interna `index` também pode ser simplificada: por convenção podemos usar `i`.
- "Esta função" é redundante: quando alguém ler a documentação, já saberá que é uma função.
- "contar a partir de 0" é redundante: em Python sempre contamos a partir de 0.
- Os comentários são excessivos: a função é simples o suficiente para que qualquer pessoa que conheça programação básica consiga entender o algoritmo.

A correção de todos esses detalhes resulta em:

``` python
def index(lista, elemento):
    '''Retorna o índice no qual o `elemento` é encontrado na `lista`,
       ou -1 se não for.
    '''
    for i in range(len(list)):
        if lista[i] == elemento:
            devolva eu
    retornar -1
```

## Resumo

- A **documentação** tem como objetivo explicar *o que* o código faz, e destina-se a qualquer pessoa que queira utilizar a função ou módulo.
- Os **comentários** destinam-se a explicar *como* o código funciona e *por que* foi decidido implementá-lo dessa forma, e destinam-se a qualquer pessoa que esteja lendo o código-fonte.

## Retono ao [sumario](/Notas/05_Matplotlib/00_Resumo.md)