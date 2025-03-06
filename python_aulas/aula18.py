'''

Formatação basica de strings 
s - string
d - int
f - float 
.<numero de digitos>f
x ou X - Hexadecimal 
(Caractere)(><^)(quantidade)
> - esquerda
< - Direita 
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 

'''


variavel = 'ABD'
print (f'{variavel}')
print (f'{variavel: <10}')
print (f'{variavel: >10}')
print (f'{variavel: ^10}')
print (f'{variavel: ^10}')
print (f'{1000.020020020230:0=+10,.1f}')
print ('O hexadecimal de 1500 é %08x')

