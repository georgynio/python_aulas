# Contadores do módulo _collections_

O módulo [collections](https://docs.python.org/pt-br/3/library/collections.html?highlight=collections#module-collections) oferece objetos úteis para manipulação de dados.

## Exemplo: Contar coisas

Digamos que você queira fazer uma tabela com o número total de caixas para cada fruta.

``` python
caminhao = [
    ('Pera', 100, 490.1),
    ('Laranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Laranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]
```

Existem duas entradas `Laranja` e duas `Pera` nesta lista. Essas caixas devem ser combinadas de alguma forma.

## Contadores

Solução: Use o `Couter`.

``` python
# utilizando o module Counter
from collections import Counter
total_caixas = Counter()
for nome, n_caixas, preco in caminhao:
    total_caixas[nome] += n_caixas

total_caixas['Laranja'] # 150
total_caixas['Pera'] # 175

# do modo tradicional
total_caixas = 0
for caixa in caminhao:
    if 'Laranja' in caixa:
        total_caixas += caixa[1]
print(f'Laranja {total_caixas}')

# para o caso da pera devemos repetir if
```

## Retorno ao [sumário](./00_Resumo.md)