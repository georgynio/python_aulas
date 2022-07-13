# Problemas de design

## Arquivos versus iteráveis

Compare esses dois programas que resultam na mesma saída.

``` python
# Precisa do nome de um arquivo
def read_data(file_name):
    registros = []
    with open(file_name) as f:
        for linha in f:
            ...
            registros.append(r)
    return registros

d = read_data('arquivo.csv')
```

``` python
# Precisa de linhas de texto
def read_data(linhas):
    registros = []
    for linha in linhas:
        ...
        registros.append(r)
    return registros

with open('file.csv') como f:
    d = read_data(f)
```

* Qual das funções `read_data()` você prefere e por quê?
* Qual das funções permite maior flexibilidade?

## Uma ideia profunda: "Duck Typing"

[Duck Typing](https://en.wikipedia.org/wiki/Duck_typing) do inglês ou português ["Duck Typing"](https://pt.wikipedia.org/wiki/Duck_typing) é um conceito usado na programação para determinar se um objeto pode ser usado para uma finalidade específica. Esta é uma aplicação específica do [teste do pato](https://pt.wikipedia.org/wiki/Teste_do_pato), que pode ser resumido da seguinte forma:

> Se parece com um pato, nada como um pato e grasna como um pato, então provavelmente é um pato.

Enquanto a primeira versão de `read_data()` requer especificamente um arquivo de texto, a segunda versão funciona com *qualquer* iterável.

``` python
def read_data(linhas):
    registros = []
    for linha in linhas:
        ...
        registros.append(r)
    return registros
```

O Duck Typing é um estilo de programação que não procura o tipo do objeto para determinar se ele tem a interface correta. Ao invés disso, o método ou atributo é simplismente chamado ou usado ('se parece como um pato e grasna como um pato, então deve ser um pato'). Isso implica que podemos usá-lo com outros tipos de *linhas*, não necessariamente com arquivos. Vejamos alguns exemplos:

``` python
# Um arquivo .csv
linhas = open('data.csv')
dados = read_data(linhas)

# Um arquivo compactado
linhas = gzip.open('data.csv.gz','rt')
dados = read_data(linhas)

# A entrada padrão (Standard Input), pelo teclado
linhas = sys.stdin
dados = read_data(linhas)

# Uma lista de strings
linhas = ['Quinoto,50,91,1','Laranja,75,123,45', ... ]
dados = read_data(linhas)
```

Então os nossos "patos" serão as `linhas`  que iremos passar para a função `read_data()`.

## Práticas recomendadas no design de bibliotecas

As bibliotecas de código costumam ser mais úteis se forem flexíveis. Não restrinja as opções desnecessariamente. Com maior flexibilidade geralmente está associado maior poder.

## Retono ao [sumario](/Notas/05_Matplotlib/00_Resumo.md)