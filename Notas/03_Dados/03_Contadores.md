# Contadores do módulo _collections_

O módulo `collections` oferece objetos úteis para manipulação de dados.

### Exemplo: Contar coisas

Digamos que você queira fazer uma tabela com o número total de caixas para cada fruta.

``` python
caminhao = [
    ('Pera', 100, 490,1),
    ('Laranja', 50, 91,1),
    ('Caqui', 150, 83,44),
    ('Laranja', 100, 45,23),
    ('Pera', 75, 572,45),
    ('Lima', 50, 23.15)
]
```

Existem duas entradas `Orange` e duas `Pear` nesta lista. Essas gavetas devem ser combinadas de alguma forma.

### Contadores

Solução: Use um `Contador`.

``` python
from collections import Counter
total_drawers = Counter()
for nome, n_gavetas, preco in caminhao:
    total_drawers[nome] += n_drawers

total_drawers['Orange'] # 150
```





Retono ao [sumario](/Notas/03_Dados/00_Resumo.md)