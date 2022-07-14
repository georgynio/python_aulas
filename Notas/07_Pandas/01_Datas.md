# Manipulação de datas e horários

## O módulo de data e hora

A seguir apresentamos o módulo `datetime` que nos permite trabalhar com datas e horas. Este módulo define um novo tipo de objeto: `datetime` (sim, com o mesmo nome do módulo), que nos permite representar um instante de tempo (data e hora). Também define objetos do tipo `date` para representar apenas uma data e do tipo `time` para armazenar e trabalhar com horários.

### Exemplo: Obter data e hora atuais

``` python
>>> import datetime 

>>> date_time = datetime.datetime.now()
>>> print(date_time)
2022-07-13 18:39:05.741169
```

### Exemplo: Obter data atual

Podemos obter apenas a data:

``` python
>>> data = datetime.date.today()
>>> print(data)
2022-07-13
```

**O que há dentro do módulo datetime?**

Em Python podemos usar a função `dir()` para obter uma lista de todos os atributos de um módulo.

``` python
>>> print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__',
 '__loader__', '__name__', '__package__', '__spec__', '_divide_and_round',
 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
```

Vamos nos concentrar no mais usado de `datetime`:

* date
* time
* datetime
* timedelta

## A classe datetime.date

Você pode gerar objetos do tipo data com a classe `date`. Um objeto desta classe representa uma data (ano, mês, dia).

### Exemplo: Um objeto para representar uma data

```python
>>> d = datetime.date(2019, 4, 13)
>>> print(d)
2019-04-13
```

O comando `date()` neste exemplo constrói um objeto do tipo `date`. Este _construtor_ recebe três argumentos: ano, mês e dia.

Também poderíamos importar diretamente a classe `date` do módulo `datetime`:

```python
>>> from datetime import date
>>>
>>> d = date(2019, 4, 13)
>>> print(d)
2019-04-13
```

### Exemplo: Obter a data de um timestamp

Em sistemas operacionais derivados do Unix (Mac OS X, Linux, etc.) o número de segundos decorridos desde o primeiro de janeiro de 1970 às 0 horas UTC até o momento a ser representado é tomado como medida de tempo. É conhecido como Unix timestamp. Você pode converter um timestamp em uma data usando o método `fromtimestamp()`.

```python
>>> from datetime import date
>>>
>>> timestamp = date.fromtimestamp(1326244364)
>>> print('Data =', timestamp)
Data = 2012-01-10
```

### Exemplo: Obtenha o ano, mês e dia separadamente

``` python
from datetime import date

hoje = date.today()

print('Ano atual:', hoje.year)
print('Mês atual:', hoje.month)
print('Dia atual:', hoje.day)
print('Day of the week:', hoje.weekday()) # vai de 0 a 6 começando na segunda
```

## A classe datetime.time

Um objeto da classe `time` representa a hora local (independentemente da configuração do seu computador).

### Exemplo: Representando o tempo com um objeto `time`

A classe `time` é usada para representar tempos.

``` python
>>> from datetime import time
>>>
>>> a = time() # time(hora = 0, minuto = 0, segundo = 0)
>>> print('a =', a)
a = 00:00:00

>>> b = time(11, 34, 56)
>>> print('b=', b)
b = 11:34:56

>>> c = time(hour = 11, minute = 34, second = 56)
>>> print('c=',c)
c=11:34:56

>>> d = time(11, 34, 56, 234566) # time(hora, minuto, segundo, microssegundo)
>>> print('d=',d)
d = 11:34:56.234566
```

### Exemplo: obter horas, minutos, segundos e microssegundos

Depois de criar um objeto `time`, você pode extrair seus atributos assim:

``` python
from datetime import time

a = tempo (11, 34, 56)

print('hora =', a.hour)
print('minuto =', a.minute)
print('segundo =', a.second)
print('microsegundo =', a.microsecond)
```

## A classe datetime.datetime

Como já mencionado, o módulo `datetime` possui uma classe de mesmo nome que permite armazenar informações de data e hora em um único objeto.

### Exemplo: objeto datetime

``` python
>>> from datetime import datetime

>>> # datetime(ano, mês, dia)
>>> a = datetime(2020, 4, 21)
>>> print(a)
2020-04-21 00:00:00

>>> # datetime(ano, mês, dia, hora, minuto, segundo, microssegundo)
>>> b = datetime(2021, 4, 21, 6, 53, 31, 342260)
>>> print(b)
2021-04-21 06:53:31.342260
```

### Exemplo: Obter ano, mês, dia, hora, minuto, timestamp de um datetime

O código a seguir gera um objeto `datetime` com valores passados ​​como parâmetros, e então imprime as informações.

``` python
from datetime import datetime

a = datetime(2021, 4, 21, 6, 53, 31, 342260)
print('año =', a.year)
print('mes =', a.month)
print('día =', a.day)
print('hora =', a.hour)
print('minuto =', a.minute)
print('timestamp =', a.timestamp())
```

## A classe datetime.timedelta

Um objeto `timedelta` representa uma duração, ou seja, a diferença entre dois instantes de tempo.

### Exemplo: Diferença entre datas e horas

``` python
>>> from datetime import datetime, date

>>> t1 = date(year = 2021, month = 4, day = 21)
>>> t2 = date(year = 2020, month = 8, day = 23)
>>> t3 = t1 - t2
>>> print(t3)
241 days, 0:00:00

>>> t4 = datetime(year = 2020, month = 7, day = 12, hour = 7, minute = 9, second = 33)
>>> t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)
>>> t6 = t4 - t5
>>> print(t6)
-333 days, 1:14:20

>>> print('tipo de t3 =', type(t3))
tipo de t3 = <class 'datetime.timedelta'>

>>> print('tipo de t6 =', type(t6))
tipo de t6 = <class 'datetime.timedelta'>
```

### Exemplo: Diferença entre objetos timedelta

``` python
>>> from datetime import timedelta

>>> t1 = timedelta(weeks = 1, days = 2, hours = 1, seconds = 33)
>>> t2 = timedelta(days = 6, hours = 11, minutes = 4, seconds = 54)
>>> t3 = t1 - t2

>>> print('t3 =', t3)
2 days, 13:55:39
```

`t3` também é do tipo `<class 'datetime.timedelta'>`.

### Exemplo: Imprimir objetos timedelta negativos

``` python
>>> from datetime import timedelta

>>> t1 = timedelta(seconds = 21)
>>> t2 = timedelta(seconds = 55)
>>> t3 = t1 - t2

>>> print(t3)
-1 day, 23:59:26

>>> print(abs(t3))
0:00:34
```

### Exemplo: duração em segundos

Você pode obter o tempo medido em segundos usando o método `total_seconds()`.

``` python
>>> from datetime import timedelta

>>> t = timedelta(days = 1, hours = 2, seconds = 30, microseconds = 100000)
>>> print('segundos totais =', t.total_seconds())
segundos totaiss = 93630.1
```

> Você também pode adicionar datas e horas usando o operador `+`. Você também pode multiplicar ou dividir um objeto `timedelta` por inteiros ou floats.

## Formato para datas e horas

Existem várias formas de representar o tempo, que variam de acordo com o lugar, a organização, etc. Por exemplo, na Argentina costumamos usar `dd/mm/aaaa`, enquanto nas culturas anglo-saxônicas é mais comum usar `mm/dd/aaaa`.

Em Python temos os métodos `strftime()` e `strptime()` para lidar com isso.

### Python strftime() - converte um objeto datetime em uma string

O método `strftime()` é definido nas classes `date`, `datetime` e `time`. Esse método cria uma string de formato desses objetos.

### Exemplo: formato de data usando strftime()

``` python
>>> from datetime import datetime

>>> now = datetime.now()

>>> t = now.strftime('%H:%M:%S')
>>> print('hora:', t)
hora: 14:40:06

>>> s1 = now.strftime('%m/%d/%Y, %H:%M:%S')
>>> # en formato mm/dd/YY H:M:S
>>> print('s1:', s1)
s1: 09/24/2020, 14:40:06


>>> s2 = now.strftime('%d/%m/%Y, %H:%M:%S')
>>> # en formato dd/mm/YY H:M:S
>>> print('s2:', s2)
s2: 24/09/2020, 14:40:06

```

Aqui, `%Y`, `%m`, `%d`, `%H` etc. são códigos de formato. O método `strftime()` pega um ou mais códigos de formato e retorna a string formatada com base nesses códigos.

No programa acima, `t`, `s1` e `s2` são strings. E os códigos de formato são:

* `%Y` - ano [0001,..., 2018, 2019,..., 9999]
* `%m` - mês [01, 02, ..., 11, 12]
* `%d` - dia [01, 02, ..., 30, 31]
* `%H` - hora [00, 01, ..., 22, 23
* `%M` - minuto [00, 01, ..., 58, 59]
* `%S` - segundo [00, 01, ..., 58, 59]

Para saber mais sobre `strftime()`, visite [a documentação](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior).

### Python strptime() - converte uma string em um objeto datetime

O método `strptime()` cria um objeto `datetime` de uma string.

### Exemplo: strptime()

``` python
>>> from datetime import datetime

>>> string_with_date= '21 de setembro de 2021'
>>> print('data_string =', string_with_date)
date_string = 21 de setembro de 2021

>>> date_object = datetime.strptime(string_with_date, '%d %B, %Y')
>>> print('data_object =', data_object)
data_object = 21-09-2021 00:00:00
```

O método `strptime()` recebe dois argumentos:

* uma string representando uma data e hora
* um código de formato correspondente ao primeiro argumento

Os códigos de formato `%d`, `%B`, `%Y` representam `day`, `month` (nome completo) e `year` respectivamente.

Consulte [a documentação](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) para obter mais detalhes.

## Retono ao [sumario](/Notas/07_Pandas/00_Resumo.md)