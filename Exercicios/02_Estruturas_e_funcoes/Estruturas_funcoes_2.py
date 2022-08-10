# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 14:05:37 2022

@author: georgynio
"""

# resp. laryssa
def soma_l(n):
    total = 0
    a = n
    while n > 0:
        total += a
        print(a, n)
        n -= 1
    return total

def soma_l(n):
    total = 0
    for _ in range(n):
        total += n
    return total

print(soma_l(4))
# print(soma_l('a'))

# resp. karine
def soma_k(n):
    total = n*n 
    return total

def soma_k(n):
    return n*n

print(soma_k(4))
print(soma_k('karine'))
print(soma_k('a'))


