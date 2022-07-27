# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

3*4
#print(_)



#%% Tabela
a = 3

print(a,'*', 0, '=', a*0)
print(a,'*', 1, '=', a*1)
print(a,'*', 2, '=', a*2)
print(a,'*', 3, '=', a*3)
print(a,'*', 4, '=', a*4)
print(a,'*', 5, '=', a*5)
print(a,'*', 6, '=', a*6)
print(a,'*', 7, '=', a*7)
print(a,'*', 8, '=', a*8)
print(a,'*', 9, '=', a*9)

#%%
print('\nUtilizando print tradicional \n\n')
a=3
for i in range(10):
    print(a,'*', 0, '=', a*i)


#%% uso do for

print('\nUtilizando format \n\n')
a=3
for i in range(10):
    #print(a,'*', 0, '=', a*i)
    print('{0} * {1} = {2:5d}'.format(a, i, a*i))

#%%
print('\nUtilizando f-string \n\n')

for i in range(10):
    print(f'{a} * {i} = {i*a}')

#%% uso do while
i = 0
while i<10:
    print(i)
    i = i+1

