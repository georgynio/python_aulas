# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 14:35:37 2022

@author: georgynio
"""

s = ('maçã', 100, 490.1)

fruta, quantidade, preco = s

print(f'Preço das frutas: { quantidade*preco}')
print(f'Preço das frutas: {s[1]*s[2]}')

#%%

# criar um dicionario onde os indices sejam
# os nomes dos alunos
# os valores dentro são: estatura, idade, peso

alunos = {
    'wallace': [1.70, 25, 79],
    'alexsander': [1.90, 42, 110],
    'alexandre': [1.87, 49, 98],
    'laryssa': [1.65, 27, 65],
    'miriam': [1.64, 33, 58],
    'karine': [1.63, 29, 50],
    'philip': [1.80, 25, 82],
    'yossimar': [1.70, 32, 74]
    }

for aluno in alunos:
    print(f'nome: {aluno}, estatura: {alunos[aluno][0]}, idade: {alunos[aluno][1]}, peso: {alunos[aluno][2]}')