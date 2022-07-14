# Gerenciar arquivos e pastas

## Gerenciando arquivos e diretórios

Uma pasta ou diretório é uma coleção de arquivos e diretórios. Python tem o módulo `os` que oferece muitas ferramentas úteis para trabalhar com diretórios e arquivos.

Nesta seção você aprenderá como criar um diretório, renomeá-lo, listar todos os seus arquivos e subdiretórios, etc.

### Obtenha o diretório atual

Para obter o diretório de trabalho atual, usamos a função `getcwd()` (_get current working directory_) do módulo `os`.

Esta função retorna o diretório atual como uma string.

``` python
>>> import os
>>> os.getcwd()
'/home/user/python/exercises'
```

É importante observar que a saída dependerá do sistema operacional que você está usando. Por exemplo, no Windows você pode obter algo assim: `C:\username\python\exercises`.

### Alterar diretório de trabalho

Você pode alterar os diretórios usando a função `chdir()` (_change directory_). Os diretórios podem ser relativos ou absolutos (em sistemas operacionais baseados em Unix, '.' é o diretório atual, '..' é o anterior, '/' é o diretório raiz).

``` python
>>> os.chdir('../Data') # digite ../Data
>>> print(os.getcwd())
/home/user/python_exercises/Data
>>> os.chdir('..') # sobe um nível
>>> os.chdir('..') # sobe outro nível
>>> print(os.getcwd())
/home/user/
>>> os.chdir('/home')
>>> print(os.getcwd())
/home
```

Para alterar os diretórios, você passa o novo diretório como uma string para esta função.

Em diferentes sistemas operacionais, as barras de diretório são escritas de maneiras diferentes. Recomenda-se usar o comando `os.path.join`:

``` python
>>> diretorio = os.path.join('/home', 'user', 'python_exercises')
>>> os.chdir(diretorio)
>>> diretorio
'/home/user/python_exercises'
```

No caso de usá-lo no Windows, será semelhante a:

``` python
>>> diretorio = os.path.join('c:\\', 'user', 'python_exercises')
>>> os.chdir(diretorio)
```

>**O uso de diretórios relativos ao atual (começando com `./`) e não absolutos (começando com `/`) facilita a portabilidade do código de um computador para outro.**

## Listar diretórios e arquivos

A função `listdir()` pega um diretório (*path*) e retorna uma lista de todos os arquivos e subdiretórios em um diretório.

``` python
>>> os.getcwd()
'/home/user/python_exercises'
>>> os.listdir()
['src', 
'pyvenv.cfg', 
'bin', 
'.gitignore', 
'lib', 
'share']
```

## Crie um novo diretório

Você pode criar um diretório com a função `mkdir()`. Funciona de forma semelhante ao `mkdir` do Unix.

``` python

>>> os.mkdir('test') # cria diretório de teste
>>> os.mkdir(os.path.join('test', 'arquivo_1')) # cria uma pasta de subdiretório dentro de test
>>> os.listdir('teste')
['arquivo_1']
```

## Renomeie um diretório ou um arquivo

Para renomear um diretório ou arquivo, a função `rename()`.

``` python
>>> os.chdir('test') # digite o diretório de teste
>>> os.listdir()
['folder']
>>> os.rename('folder','new_folder') # renomear pasta
>>> os.listdir()
['new_folder']
```

## Excluir um diretório ou um arquivo

> :warning: **A seguir, usaremos comandos que excluem arquivos sem passar por nenhuma lixeira. Essas ações não podem ser desfeitas**: Use com cautela, _com grandes poderes vêm grandes responsabilidades_.

Você pode remover um arquivo usando a função `remove()`. Para remover um diretório deve usar `rmdir()`.

No código a seguir trabalharemos em uma pasta que possui essa estrutura:

```bash
outra_pasta
├── arquivo.txt
└── subpasta
```

``` python
>>> os.chdir('outra_pasta') # digite outra pasta que tenha
                                # uma subpasta e um arquivo de texto
>>> os.listdir()
['subpasta', 'arquivo.txt']

>>> os.remove('arquivo.txt') # remove o arquivo
>>> os.listdir()
['subpasta']

>>> os.rmdir('subpasta') # exclui a subpasta
>>> os.listdir()
[]
```

**Aviso**: `rmdir()` só pode deletar diretórios se estiverem vazios.
Para remover um diretório não vazio, você pode usar `rmtree()` do módulo `shutil`.

``` python
>>> os.mkdir(os.path.join('test','folder')) # cria nova pasta
                                                            # teste interno
>>> os.mkdir(os.path.join('test','folder', 'subfolder')) # cria uma subpasta na pasta
>>> os.chdir('teste') # digite teste
>>> os.rmdir('folder') # Quero deletar a pasta
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [Errno 39] Directory not empty: 'pasta'

>>> import shutil

>>> shutil.rmtree('pasta')
>>> os.listdir()
[]
```

## Diretórios andando com `os.walk()`

A função `walk()` do módulo `os` gera uma lista dos nomes de todos os arquivos na árvore de subdiretórios de um determinado diretório. Ou seja, ele lista os arquivos em um determinado diretório e depois entra em cada subdiretório e faz a mesma coisa, recursivamente (_top-down_).

A função `walk()` recebe como único parâmetro obrigatório o diretório onde começar a caminhar (a raiz da árvore).

### Exemplo

Este exemplo mostra como `os.walk()` é usado.

```python
import os
for root, dirs, files in os.walk("."):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
```

## Retono ao [sumario](./00_Resumo.md)