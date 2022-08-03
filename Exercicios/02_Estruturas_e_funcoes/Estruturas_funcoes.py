# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 14:55:00 2022

@author: georgynio
"""

# vamos a conferir a pasta  a onde nos encontramos
import os

os.getcwd()

#%%
# abrir o arquivo utilizando o comando open()
file = open('C:/Users/georgynio/Desktop/2020ES.csv', 'r')
#file.read()

for i in range(20):
    linha = file.readline()
    print(linha.split(','))

# exemplo utilizando o pandas
import pandas as pd

dados = pd.read_csv('C:/Users/georgynio/Desktop/2020ES.csv', encoding='cp1252')
dados.head()
#%%
with open('C:/Users/georgynio/Desktop/2020ES.csv') as file:
    file.read()