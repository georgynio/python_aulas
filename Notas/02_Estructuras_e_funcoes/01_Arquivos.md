# Gerenciamento de archivos

É de grande importância para qualquer programador saber manipular arquivos, seja para criar backups, consumir uma lista de alguma planilha ou qualquer motivo que seja. 

## Arquivos de entrada e saida

Incialmente podemos usar a função `open`, para abrir o arquivo em modo leitura e escritura:

```python
f = open('foo.txt', 'rt')     # Abre o arquivo em modo leitura ('r' de read, 't' de text)
g = open('bar.txt', 'wt')     # Abre o aquivo em modo escritura ('w' de write, 't' de text)
```

_Observação: os nomes [foo, bar, foobar](https://es.wikipedia.org/wiki/Foo) são nomes comuns, que se usam gerlamente para se referir a um nome que se ignora, são os equivalente a fulano, mengano e zutano._

Para ler o arquivo completo, ou apenas uma parte:

```python
data = f.read()

# Ler 'maxbytes' bytes
data = f.read([maxbytes])
```

Para escrever um texto no arquivo:

```python
g.write('alguma coisa')
```

E. finalmente, fechar os arquivos.

```python
f.close()
g.close()
```

Para evitar problemas é muito importante fechar os arquivos, porém, é comum esquecer disso. Para que isto não aconteça o Python tem o comando `with` e pode ser usado da seguinte forma:

```python
with open(nome_archivo, 'rt') as file:
    # Usa o pseudônimo do arquivo `file`
    ...comandos
    # Não precisa colocar "arquivo.close()"
...comandos que não interagem com o arquivo
```

Essa estrutura fecha o arquivo ao terminar de executar os comandos do bloque identado.

**Nota:** Em alguns casos devemos especificar o tipo de \_encoding\_ agregando `encoding='utf8'` como parâmetro do comando `open`.

## Comandos usuais para ler um arquivo

Para ler um arquivo inteiro, de uma só vez, como uma string:

```python
with open('foo.txt', 'rt') as file:
    dado = file.read()
    # `dado` é uma string com *todo* o texto em`foo.txt`
```

Para ler linha por linha iterativamente:

```python
with open(nome_arquivo, 'rt') as file:
    for line in file:
        # Processa cada linha
```

## Comandos usuais para escrever um arquivo

Para escrever strings:

```python
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
    ...
```

Você também pode redirecionar a saída de impressão (da tela para um arquivo).

```python
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
    ...
```

***Nota:*** Maior informação pode ser encontrada na docomentação [leitura e escrita de arquivos](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) do python.

## Retorno ao [sumário](./00_Resumo.md)