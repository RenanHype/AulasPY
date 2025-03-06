'''
Repetições:

while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um codigo nao tem fim
'''

condicao = True

while condicao:
    idade = input('Qual é a sua idade? ')
    if idade == 'Sair':
        break
    if idade.isdigit():
        idade = int(idade)
        if idade >= 18:
            print('Você é maior de idade')
            break
        else:
            print('Você é menor de idade, por favor repita o processo')
    else:
        print('Digite uma idade válida(apenas números, EX: 19) ')
