entrada = input('[E]ntrar [S]air ')
senha_digitada = input('Senha: ')
senha_permitida = 'Renan@2809'




if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print ('Senha Incorreta')




# Avaliação de curto circuito, exemplo; o codigo abaixo parou no false:
#print(True and False and True)


'''if 1 and 1:
    print(1 and 2)'''

