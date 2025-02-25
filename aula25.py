"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
    
#Exercicio um
 
'''
entrada = input('Digite um número: ')

if entrada.isdigit():
    entradaint = int(entrada)
    par_impar = entradaint % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entradaint} é {par_impar_texto}')
else:
    print('Não é um número inteiro')  
'''

#Exercicio dois


'''horario = input('Digite um horário (0-23): ') 
horario_int = float(horario) 

if horario.isdigit(): 
    if horario_int < 0 or horario_int > 24:
        print('Horário inválido')
    else:
        if horario_int < 12:
            print('Bom dia')
        elif horario_int < 18:
            print('Boa tarde')
        else:
            print('Boa noite') '''


#exercicio tres


nome = input('Digite seu nome: ').strip()
n_letras = len(nome)

if n_letras == 0:
    print('Você não digitou nada')
elif n_letras <= 1:
    print('Digite mais que uma letra por favor')
elif 1 < n_letras <= 4:
    print(f'Seu nome tem', n_letras, 'letras e é curto') 
elif 4 < n_letras <= 6:
    print(f'Seu nome tem', n_letras, 'letras e é normal')
else: 
    print(f'Seu nome tem', n_letras, 'letras e é grande')
