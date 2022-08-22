# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:15:01 2022

@author: georgynio
"""

from collections import Counter

arr = [1, 2, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5]

print(Counter(arr))


def contar(lista):
    d_lista = {}
    for i in lista:
        if i in d_lista:
            d_lista[i] += 1
            print(f'elemento antigo {i}')
            print(d_lista)
        else:
            d_lista[i] = 1
            print(f'elemento novo {i}')
            print(d_lista)
    return d_lista

contar(arr)
print(Counter(arr))

#%%

def formato_1(linha_f):
    ll = linha_f.split(',')
    return f'{ll[0]} {ll[1]} {ll[2]}'


dado = open('C:/Users/georgynio/Desktop/agricultura-produo-brasil.csv', 'r', encoding='utf8')

dado_read = dado.readlines()

for linha in dado_read[1:10]:
    print(formato_1(linha))
    
