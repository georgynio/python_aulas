# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 14:27:53 2022

@author: georgynio
"""

line = 'Pera,100,490.10'

row = line.split(',')
row


#%%

# cuidado com o decimal

line = 'Pera;100;490,10'

row = line.split(',')
row


#%%

nomes = ['wallace', 'thiago', 'celeste', 'laryssa']


nomes.append('karine')


for i in range(4):
    nomes.append(i)
    
    
lista = ['felipe', 'joao', 'maria', 'pedro']

for i in lista:
    nomes.append(i)
    
#%% colocar a maria na posição 2

nomes = ['wallace', 'thiago', 'celeste', 'laryssa']
nomes.sort()
nomes


#%% f-string

line = 'Açucar,5,30'

print(f'lista: {line}')
prod, peso, valor = line.split(',')

print(f'\tproduto:\t {prod}')
print(f'\tpeso:\t\t {peso} kg')
print(f'\tvalor:\t\t {valor} R$')

prod_1 = ['açucar', 5, 30]
prod_2 = ['feijão', 10, 50]

print('--'*10)
print(f'produto: {prod_1[0]} \npeso:\t {prod_1[1]} \nvalor:\t {prod_1[2]}')
print('--'*10)
print(f'produto: {prod_2[0]} \npeso:\t {prod_2[1]} \nvalor:\t {prod_2[2]}')
