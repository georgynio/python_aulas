# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def ler_formatar(csv_file):
    dados = csv_file.readlines()
    cab_1, cab_2, cab_3 = dados[1].split(',')
    for linha in dados[2:-2]:
        c1, c2, c3 = linha.split(',')
        return f'{c1:>10s}|{c2:10s}|{c3:10s}'
    


with open('C:/Users/georgynio.aylas/Desktop/aulas_python/agricultura-produo-brasil.csv.txt', 'r', encoding='utf8') as agr_csv:
    print(ler_formatar(agr_csv))
    

