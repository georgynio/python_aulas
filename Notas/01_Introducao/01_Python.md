# Python

## O que é?

Python é uma linguagem interpretada de alto nível, que suporta multiplos paradigmas da programação: imperativo, orientado a objetos e funcional. Classificado como uma linguagem de ["scripting"](https://pt.wikipedia.org/wiki/Linguagem_de_script), já que não precisa ser compilado. 

Criado por Guido van Rossum, lançada por primeira vez em 1991, deve seu nome ao grupo de comedia britanico ["Monty Python"](https://pt.wikipedia.org/wiki/Monty_Python)

### Onde podemos consegui-lo?

Normalmente as diferentes versões do [Python](https://www.python.org/) estão disponiveis no site de [descarga](https://www.python.org/downloads/). Mas tome cuidado na hora instalar se o objetivo é usar alguma biblioteca específica do Python.

### Estamos quase prontos para começar a brincar com o Python

Dos diferentes entornos possiveis de executar o Python o de uso mais frequente é desde o terminal. Para começar, coloca no terminal `python`, ele ira executar o programa:

```bash
bash$ python
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hello world")
hello world
>>>
```

Caso precise de uma ajuda sobre o uso do terminal leia o [tutorial curto](https://tutorial.djangogirls.org/pt/intro_to_command_line/), nesta vai encontrar informação basica sobre o ambiente.

## Começando pelo começo

### Python como  calculadora?

Sim, prova a realizar o seguinte exemplo:

- Converte 100km a pes (1 pé = 0,3048 metros).

- Reparte 3 maças para 4 pessoas

```python
>>> 100*1000*(0.3048)
30480
>>> 3 / 4
0.75
```

**tip**: o carater underline ( _ ) serve para usar o resultado do ultimo calculo.

- Quantas partes de uma maça come cada pessoa se inicialmente tivemos 6.

```python
>>> _*2
1.5
```

### Pedindo ajuda ao Python

No terminal escreva `help()`:

```python
>>> help
Type help() for interactive help, or help(object) for help about object
```

Esta ferramenta ajuda bastante quando não se lembra de como usar alguma biblioteca. Porém, não funciona para os comandos básicos tipo: `for`, `if`, `while`, etc. nesse caso a resposta sera um erro.

```python
>>> help(for)
  File "<stdin>", line 1
    help(for)
         ^
SyntaxError: invalid syntax
```

As veces funciona quando colocando aspas `help('for')`. Para encontrar a documentação completo se recomenda a visita no site oficial <http://docs.python.org>.

```python
>>> help('for') 
```

Nota: para sair do modo ajuda aperta a tecla `q`.

Para sair do interprete do Python pode usar a combinação de teclas `ctrl + d` ou escreva `exit()`.

## Retono ao [sumario](/Notas/01_Introducao/00_Resumo.md)