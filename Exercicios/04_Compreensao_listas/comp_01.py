# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:06:52 2022

@author: georgynio.aylas
"""

a = []

for i in range(10):
    a.append(i*2)
    
print(a)

b = [i*2 for i in range(10)]



#%% frutas

frutas = ['maçã', 'banana', 'cereja', 'kiwi', 'morango']

novaLista = [fruta for fruta in frutas]
print(novaLista)

#%% frutas 2

frutas = ['maçã', 'banana', 'cereja', 'milho', 'kiwi', 'morango']
print(frutas)
novaLista2 = [fruta for fruta in frutas if 'a' in fruta]
print(novaLista2)
