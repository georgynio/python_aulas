# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:23:33 2022

@author: georgynio
"""



from decimal import Decimal

x = Decimal('3.4')

#%%
for i in range(10):
    print(i)
    
    
#%% sintaxerror

# Conserta o erro e tenta ganhar o jogo.
print("**************")
print("Seja Bem Vindo")
print("**************")
numero_secreto = 65
chute = input("Digite um numero:")
print("Você digitou: ",chute)
if numero_secreto == chute:
    print("você acertou")
else:
    print("Você errou, Tente novamente")
    
#%%
# Conserta o codigo
print("exemplo de erro de sintaxe")

#%%

# Conserta o erro
print("Adicionando dois números, 2 e 3:")
print(2 + 3)

#%% 
# Conserta o erro
print("**************")
print("Seja Bem Vindo")
print("**************")
numero_secreto = 65 # string
#chute = int(input("Digite um numero:"))
chute = '65' # numero
print("Você digitou: ",chute)
if int(numero_secreto) == int(chute):
    print("você acertou")
else:
    print("Você errou, Tente novamente")

#%%

a = '3'
b = 4
print(f'A soma de a + b é: {int(a)+int(b)}')
print(f'A soma de a + b é: {str(a)+str(b)}')
print(f'A soma de a + b é: {float(a)+float(b)}')

#%%
a = [4]
b = 3

# errado
if a+[b] == [3, 4]:
    print(a+b)

# errado
a.append(b)
print(a)
if a == [3, 4]:
    print(a+b)

# 
a = [4]
b = [3]
if b + a == [3, 4]:
    print(a+b)

#%% erro de semantica

a = 3
b = 4
print(f'O produto de a e b é: {a*b}')    
    
#%%

a = 4
b = 3

if not list(a*b):
    print(a*b)
else:
    print('Algo de errado não esta certo!')
    print('Eu queria a resposta de 3*4')
    