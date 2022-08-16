# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:05:58 2022

@author: georgynio
"""

lista = ['Joana', 'Edmundo', 'Rosita']


for i, nome in enumerate(lista):
    dado = nome.split()
    print(i, dado)
    #print(i, nome)
    
    
#%%

arquiv = open(...)

dado = arquivo.read()

for i, linha in enumerate(dado):
    dado_linha = linha.split(',')
    print(dado_linha)