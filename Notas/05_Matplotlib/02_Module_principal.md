# O módulo *main*

Este módulo é o ponto de partida de qualquer programa. 

## Função *main*

Em muitos idiomas de programação existe o conceito de método de função *principal*.

``` c
//c/c++
int main(int argc, char *argv[]) {
    ...
}
```

```java
//java
classe myprog {
    public static void main(String args[]) {
        ...
    }
}
```

Consulte a função inicial que é executada ao corrigir um programa.

## Módulo *main* em Python

Python não tem uma função ou método main. Em seu lugar existe um *módulo main* e este será o arquivo com código fonte que se ejecuta primero.

```bash
bash %python3 prog.py
...
```

O arquivo que passa para o intérprete ao invocar será o módulo main. Não importa como seja chamado.

## Verifique `__main__`

É um padrão prático para usar a seguinte convenção em módulos que são executados como scripts principais:

``` python
#prog.py
...
if __name__ == '__main__':
    # Soy el programa principal ...
    comandos
    ...
```

Os comandos do `if` constituem o *programa principal*

## Módulo principal vs. módulo importado

Qual arquivo .py pode ser executado no mar como o programa principal ou como um módulo importado:

```bash
bash %python3 prog.py # Corrigindo como principal
```

``` python
import prog # Corrigindo como módulo importado
```

A variável `__name__` é o nome do módulo. Sem embargo, esta variável `__name__` valdrá `__main__` e este módulo está sendo executado como o script principal.

``` python
if __name__ == '__main__':
    # Não é executado em um módulo importado ...
```

Normalmente, mostramos que os comandos são parte do comportamento do script no modo *main*, isto irá executar apenas tudo o que o módulo *main* mandar.

Por isso, está escrito uma condição `if` que decida como se va a portar o código cuando este puede ser usado de ambas as maneras.

## Modelo de programa

Este é um modelo usual para escrever um programa em Python:

``` python
#prog.py
# Comandos import (bibliotecas o módulos)
módulos de importação

# Funções
def spam():
    ...

def blá():
    ...

# Função principal
def f_principal():
    ...

if __name__ == '__main__':
    f_principal()
```

### Ferramentas para o terminal

Python se usa muito frequentemente para rodar desde a linha de comandos. Por exemplo:

```bash
bash % python3 relatorio_final.py ../Data/caminhao.csv ../Data/precos.csv
```

Isso permite que os scripts sejam executados desde o terminal para correr processos automáticos, executar tareas em segundo plano, etc.

### Argumentos na linha de comandos

Python interpreta uma linha de comandos como uma lista de cadeias de texto.

```bash
bash % python3 relatorio_final.py ../Data/caminhao.csv ../Data/precos.csv
```

Neste caso, o leitor deve se perguntar como é feito essa leitura. O Python pode aceder a esta lista de cadeias usando `sys.argv`. Se usa o parâmetro `-i` para invocar a python de modo que o intérprete interactivo não acabar podemor avaliar os parâmetros anteriores.

```bash
bash % python3 -i informe_final.py ../Data/camion.csv ../Data/precios.csv
```

Abrindo o script `relatorio_final.py` poderemos ver o conteúdo, algo parecido com isto:

``` python
# Llamado como recién, sys.argv contiene
import sys
sys.argv # ['informe_final.py, 'camion.csv', 'precios.csv']
```

Se precisar de alguma condição específica para a leitura de dados externos, podemos coloca-los dentro de uma condição:

``` python
sistema de importação

if len(sys.argv) != 3:
    raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
camion = sys.argv[1]
precios = sys.argv[2]
...
```

Para maior informação pode verificar o módulo [argparse](https://docs.python.org/pt-br/3/library/argparse.html#module-argparse) do Python.

### I/O padrão

Os arquivos de entrada e saída são padrão (Standard Input / Output (stdio)) em arquivos que são porta como arquivos normais, mas são originados pelo sistema operacional.

``` python
sys.stdout
sys.stderr
sys.stdin
```

Por omissão, a saída impresa é dirigida a `sys.stdout` (geralmente na tela) a entrada se le `sys.stdin` (geralmente do teclado).

As entradas e saídas de *stdin* podem ser ligadas ao teclado, à pantalla, a uma impressora, a diferentes arcos ou a incluir mais coisas extra como tubos, etc.

```bash
bash %python3 prog.py > resultados.txt
#o sim não
bash %cmd1 | python3 prog.py | cmd2
```

Esta sintaxe é chamada "piping" ou redirecionamento e significa: executar cmd1, enviar sua saída como entrada para prog.py chamado do terminal, e a saída de este será a entrada para cmd2.

### Terminação do programa

A terminação e a saída do programa são administradas a travessias de exceções.

```python
raise SystemExit
raise SystemExit(codigo_salida)
raise SystemExit('Mensaje informativo')
```

O, alternativamente:

```python
import sys
sys.exit(codigo_salida)
```

É padrão que un codigo de salida de `0` indica que no hubo problemas y otro valor, que los hubo.

### O comando `#!`

Para um script em Python ser executável num sistema operativo baseado em Linux/Unix, o mesmo deve começar com o designado *shebang* (#!). Por exemplo, se agregá-la siguiente línea al comienzo de tu script podés ejecutar diretamente o script (sin invocar manualmente a Python en la misma línea).

``` python
#!/usr/bin/env python3
#prog.py
...
```

Para poder ser executado, o arquivo `prog.py` requer permissão de execução atribuída. Pode asignar da seguinte maneira:

```bash
bash % chmod +x prog.py
# agora pode executá-lo
bash % ./prog.py
... comprimentar ...
```

### Modelo de script com parâmetros

Para terminar, este é um modelo usual de programa em Python que é executado a partir do terminal.

``` python
#!/usr/bin/env python3
#prog.py

# Importar (bibliotecas)
import module

# Funções
def spam():
    ...

def blá():
    ...

# Função principal
def f_principal(parâmetros):
    # Analisar a linha de comandos,
    # usando os parâmetros variáveis ​​no lugar
    # de sys.argv, não corresponde
    ...

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
```

## Retono ao [sumario](/Notas/05_Matplotlib/00_Resumo.md)