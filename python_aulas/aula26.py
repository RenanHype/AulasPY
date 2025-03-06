'''
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutaveis que vimos: str, int, float, bool
'''

string = 'Renan'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)

print(string.zfill(10))