# Introdução aos Pandas

Em programação de computadores, pandas é uma biblioteca de software criada para a linguagem Python para manipulação e análise de dados. Em particular, oferece estruturas e operações para manipular tabelas numéricas e séries temporais.

Esta é uma breve introdução ao [Pandas](https://pandas.pydata.org/docs/getting_started/index.html). Para obter informações mais completas, recomendamos que você consulte [a documentação oficial](https://pandas.pydata.org/docs/user_guide/10min.html).

As caracteristicas desta biblioteca são:

- Usa o objeto `DataFrame` para manipulação de dados, com indexação integrada.
- Le e escreve dados entre diferentes estruturas de dados e formatos de arquivo.
- Trabalha de forma eficiente com matrizes.
- Insere e deleta colunas em conjuntos de dados.
- Possui ferramentas para fundir(merging) ou juntar(join) conjuntos de dados.
- Funciona eficientemente com séries temporais (time series).
- Auxilia na filtração e limpeza de dados.

## Leitura de dados

Antes de começar vamos conferir se temos a biblioteca pandas instalada, ao pedir a lista de bibliotecas do pip ele não estara presente. Por exemplo:

```python
🦖 ragy ❄️  python_aulas 🎁  🐋 -> pip list
Package           Version
----------------- -------
asttokens         2.0.5
backcall          0.2.0
decorator         5.1.1
executing         0.8.3
ipython           8.4.0
jedi              0.18.1
matplotlib-inline 0.1.3
numpy             1.23.1
parso             0.8.3
pexpect           4.8.0
pickleshare       0.7.5
pip               22.1.2
prompt-toolkit    3.0.30
ptyprocess        0.7.0
pure-eval         0.2.2
Pygments          2.12.0
python-dateutil   2.8.2
pytz              2022.1
setuptools        62.3.4
six               1.16.0
stack-data        0.3.0
traitlets         5.3.0
wcwidth           0.2.5
wheel             0.37.1
```

Se não estiver instalado, é só usar o `pip`.

```python
pip install pandas
```

Pandas permite que você leia vários formatos de tabelas de dados diretamente. Os dados que iremos utilizar nesta serie de exemplos estão disponiveis [no site energia e ambiente](http://energiaeambiente.org.br/qualidadedoar).

Tente o seguinte código, para ler um arquivo CSV:

```python
import pandas as pd
import os

diretorio = 'dados'
arquivo = '2020ES.csv'
fname = os.path.join(diretorio, arquivo)
df = pd.read_csv(fname, encoding='cp1252')
```

A variável `df` é do tipo `DataFrame` e contém todos os dados do arquivo csv devidamente estruturados.

```python
>>> type(df)
pandas.core.frame.DataFrame

```

Com `df.head()` você pode ver as primeiras linhas de dados. Se você passar um número para `head` como parâmetro, você pode selecionar quantas linhas deseja ver. Da mesma forma com `df.tail(n)` você verá as últimas `n` linhas de dados.

```python
>>> df.head()
         Data   Hora   Estacao Codigo Poluente  Valor Unidade        Tipo
0  2020-01-01  00:30  Carapina   ES01     MP10   10.0   ug/m3  automatica
1  2020-01-01  01:30  Carapina   ES01     MP10   14.0   ug/m3  automatica
2  2020-01-01  02:30  Carapina   ES01     MP10   12.0   ug/m3  automatica
3  2020-01-01  03:30  Carapina   ES01     MP10    4.0   ug/m3  automatica
4  2020-01-01  04:30  Carapina   ES01     MP10    8.0   ug/m3  automatica
```

Usar `df.columns` retornará uma índice com os nomes das colunas DataFrame.

```python
>>> df.columns
Index(['Data', 'Hora', 'Estacao', 'Codigo', 'Poluente', 'Valor', 'Unidade',
       'Tipo'],
      dtype='object')
>>> df.index
RangeIndex(start=0, stop=231970, step=1)
```

Otra herramienta útil para inspeccionar los datos recién levantados es `describe()`. Para ver mejor una parte, podemos seleccionar algunas columnas de interés antes de pedirle la descripción.

```python
>>> df['Valor'].describe()
count    231970.000000
mean         82.121727
std         170.106764
min           0.000000
25%           5.810000
50%          17.000000
75%          44.980000
max        2637.340000
Name: Valor, dtype: float64
```

## Seleção

Uma das operações primitivas mais importantes é a seleção de fragmentos de tabelas de dados, sejam linhas, colunas ou intervalos de linhas e colunas.

```python
>>> df['Estacao'].unique()
array(['Carapina', 'Enseada do Suá', 'Vila Velha - Ibes', 'Cariacica',
       'Cidade Continental', 'Laranjeiras', 'Jardim Camburi',
       'Vitória Centro', 'Vila Velha - Centro'], dtype=object)
```

Podemos perguntar se algum elemento se encontra em alguma coluna específica:

```python
>>> df['Estacao'] == 'Carapina'
0          True
1          True
2          True
3          True
4          True
          ...  
231965    False
231966    False
231967    False
231968    False
231969    False
Name: Estacao, Length: 231970, dtype: bool
```

Se quisermos saber a quantidade de observações específicas podemos usar `value_counts()`

```python
>>> df['Estacao'].value_counts()
Enseada do Suá         50965
Vila Velha - Ibes      41997
Cariacica              33272
Vitória Centro         29451
Laranjeiras            25454
Cidade Continental     19414
Jardim Camburi         14211
Vila Velha - Centro     8789
Carapina                8417
Name: Estacao, dtype: int64
```

Desta forma obtemos, em ordem decrescente, os nomes comuns e as quantidades das espécies mais frequentes na base de dados.

### Filtros booleanos

```python
>>> novo_df = df[df['Estacao']=='Laranjeiras']
>>> novo_df
              Data   Hora      Estacao Codigo Poluente  Valor Unidade        Tipo
154065  2020-01-01  00:30  Laranjeiras   ES05      SO2   1.57   ug/m3  automatica
154066  2020-01-01  01:30  Laranjeiras   ES05      SO2   2.15   ug/m3  automatica
154067  2020-01-01  02:30  Laranjeiras   ES05      SO2   1.64   ug/m3  automatica
154068  2020-01-01  03:30  Laranjeiras   ES05      SO2   1.31   ug/m3  automatica
154069  2020-01-01  04:30  Laranjeiras   ES05      SO2   4.02   ug/m3  automatica
...            ...    ...          ...    ...      ...    ...     ...         ...
179514  2020-12-22  11:30  Laranjeiras   ES05       O3  40.57   ug/m3  automatica
179515  2020-12-22  12:30  Laranjeiras   ES05       O3  41.84   ug/m3  automatica
179516  2020-12-22  13:30  Laranjeiras   ES05       O3  32.33   ug/m3  automatica
179517  2020-12-22  14:30  Laranjeiras   ES05       O3  29.88   ug/m3  automatica
179518  2020-12-22  15:30  Laranjeiras   ES05       O3  27.75   ug/m3  automatica

[25454 rows x 8 columns]
```

### Scatterplots

Pandas vem integrado com a biblioteca gráfica, que permite realisar [plots bonitos](https://pandas.pydata.org/docs/user_guide/visualization.html). De forma mais eficiente:

```python
df.plot.scatter(x='Data', y='Valor')
```

Existe outro módulo gráfico que interage muito bem com os pandas e se chama [Seaborn](https://seaborn.pydata.org/), este é analogo ao `ggplot` do `R`. Ele é baseado no matplotlib e oferece uma interface de alto nível para criar gráficos estatísticos atraentes e informativos.

Observe que o seaborn entende DataFrames e colunas e sua sintaxe é muito semelhante aos pandas:

```python
import seaborn as sns

sns.scatterplot(data = novo_df, x = 'Hora', y = 'Valor')
```

### Filtra por índice e posição

Como já mencionamos, o índice de `df` não possui semântica interessante. Vamos ver, em vez disso, que a série que geramos com `number_instances = df['name_com'].value_counts()` tem:

```python
>>> estacoes = df['Estacao'].value_counts()
>>> estacoes.index
Index(['Enseada do Suá', 'Vila Velha - Ibes', 'Cariacica', 'Vitória Centro',
       'Laranjeiras', 'Cidade Continental', 'Jardim Camburi',
       'Vila Velha - Centro', 'Carapina'],
      dtype='object')

```

`cant_ejemplares` es una serie (es como un DataFrame de una sola columna). Tiene los nombres de las especies como índice y sus respectivas cantidades como dato asociado.

Podemos acceder a una fila de un DataFarme o una Serie tanto a través de su posición como a través de su índice. Para acceder con el índice usá `loc[]` como en los siguientes ejemplos:

```python
>>> df.loc[165]
long                                                   -58.4684
lat                                                    -34.6648
id_arbol                                                    166
altura_tot                                                    5
diametro                                                     10
inclinacio                                                    0
id_especie                                                   11
nombre_com                                            Jacarandá
nombre_cie                                Jacarandá mimosifolia
tipo_folla                        Árbol Latifoliado Caducifolio
espacio_ve                                        INDOAMERICANO
ubicacion     LACARRA, Av. - ESCALADA, Av. - CASTAÑARES, Av....
nombre_fam                                         Bignoniáceas
nombre_gen                                            Jacarandá
origen                                         Nativo/Autóctono
coord_x                                                 99534.3
coord_y                                                 96061.8
Name: 165, dtype: object

>>> cant_ejemplares.loc['Eucalipto']
4112
```

Para acceder por número de posición usá `iloc`, como se muestra a continuación.

```python
>>> df_jacarandas.iloc[0]
altura_tot     5
diametro      10
inclinacio     0
Name: 165, dtype: int64
```

Observá que esto nos devuelve los datos de la primera fila de `df_jacarandas` que corresponde al índice 165 (lo dice en la última línea). También podemos acceder a rebanadas (slices) usando `iloc`:

```python
>>> cant_ejemplares.iloc[0:3]
Eucalipto      4112
Tipa blanca    4031
Jacarandá      3255
Name: nombre_com, dtype: int64
```

Por otra parte, podemos seleccionar tanto filas como columnas, si separamos con comas las respectivas selecciones:

```python
>>> df_jacarandas.iloc[-5:,2]
51104     4
51172     8
51180     0
51207     0
51375    20
Name: inclinacio, dtype: int64
```

Esto nos devuelve los datos correspondientes a las últimas 5 filas y a la tercera columna ('inclinacio'). Fijate que siempre vienen acompañados del índice.

### Selección de una columna

Si queremos seleccionar una sola columna podemos especificarla por medio de su nombre. Recordemos que al tomar una sola columna obtenemos una serie en lugar de un DataFrame:

```python
>>> df_jacarandas_diam = df_jacarandas['diametro']
>>> type(df_jacarandas)
pandas.core.frame.DataFrame
>>> type(df_jacarandas_diam)
pandas.core.series.Series
```

## Series temporales en Pandas

Pandas tiene un gran potencial para el manejo de series temporales. Es muy sencillo crear índices con fechas y frecuencias seleccionadas.

```python
>>> pd.date_range('20200923', periods = 7)
DatetimeIndex(['2020-09-23', '2020-09-24', '2020-09-25', '2020-09-26',
               '2020-09-27', '2020-09-28', '2020-09-29'],
              dtype='datetime64[ns]', freq='D')

>>> pd.date_range('20200923 14:00', periods = 7)
DatetimeIndex(['2020-09-23 14:00:00', '2020-09-24 14:00:00',
               '2020-09-25 14:00:00', '2020-09-26 14:00:00',
               '2020-09-27 14:00:00', '2020-09-28 14:00:00',
               '2020-09-29 14:00:00'],
              dtype='datetime64[ns]', freq='D')

>>> pd.date_range('20200923 14:00', periods = 6, freq = 'H')
DatetimeIndex(['2020-09-23 14:00:00', '2020-09-23 15:00:00',
               '2020-09-23 16:00:00', '2020-09-23 17:00:00',
               '2020-09-23 18:00:00', '2020-09-23 19:00:00'],
              dtype='datetime64[ns]', freq='H')

```

Luego, podés usar esos índices junto con datos para armar series temporales o DataFrames:

```python
>>> pd.Series([1, 2, 3, 4, 5, 6], index = pd.date_range('20200923 14:00', periods = 6, freq = 'H'))
2020-09-23 14:00:00    1
2020-09-23 15:00:00    2
2020-09-23 16:00:00    3
2020-09-23 17:00:00    4
2020-09-23 18:00:00    5
2020-09-23 19:00:00    6
Freq: H, dtype: int64
```

### Caminatas al azar

Volviendo al tema de las caminatas al azar, podemos hacer una caminata de dos horas dando un paso por minuto a partir del comienzo de esta clase con el siguiente comando:

```python
import numpy as np

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()
```

Observá que estamos usando random del módulo numpy, no de random. La función `np.random.randint(-1,2,120)` genera un array de longitud 120 con valores -1, 0, 1 (no incluye extremo derecho del rango de valores).

Podemos ver el gráfico sencillamente:

```python
s2.plot()
```

O usar una [media móvil](https://es.wikipedia.org/wiki/Media_m%C3%B3vil) (rolling mean) para suavizar los datos:

```python
w = 5 # ancho en minutos de la ventana
s3 = s2.rolling(w).mean()
s3.plot()
```

Podés ver ambas curvas en un mismo gráfico para ver más claramente el efecto del suavizado:

```python
df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()
```

Fijate que los datos de la curva suavizada empiezan más tarde, porque al principio no hay datos sobre los cuales hacer promedio. El parámetro  `min_periods = 1` del método `rolling` te permite controlar esto. Probalo.

