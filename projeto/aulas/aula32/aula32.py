"""
Faca um programa que peca ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar, Caso o usuario nao digite um numero
inteiro, informe que nao é um nomero inteiro
"""
# numero = input('Digite um numero inteiro: ')

# MINHA
# try:
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print('Número é par')
#     else:
#         print('Numero é impar')
# except:
#     print('Nao é um numero inteiro')

# PROFESSOR
# entrada = input('Digite um numero: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'
    
#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Não é um número inteiro')

"""
Faca um programa que pergunte a hora ao usuario e, baseando-se no horario
descirto, exiba a saudacao apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
"""

# MINHA
# horas = input('Que horas são? ')

# try:
#     hora = int(horas[:2])

#     if hora >= 0 and hora < 12 :
#         print('Bom dia')
#     elif hora >= 12 and hora < 18:
#         print('Boa tarde')
#     elif hora >= 18 and hora < 24:
#         print('Boa noite')
# except:
#     print('Nao é um horario valido')

# PROFESSOR
# horas = input('Que horas são (em inteiros)? ')

# 
# hora = int(horas)

#     if hora >= 0 and hora <= 11 :
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite')
#     else:
#        print('Não conheço essa hora')
# 


"""
Faca um programa que peca o primeiro nome do usuario, Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreve
"Seu nome é normal"; maior de 6 escreve "Seu nome é muito grande"
"""

# MINHA
# nome = input('Digite seu primeiro nome: ')

# try:
#     length = len(nome)
#     if length <= 4:
#         print('Seu nome é curto')
#     elif length >= 5 and length <= 6:
#         print('Seu nome é normal')
#     else:
#         print('Seu nome é muito grande')
# except:
#     print('Nome nao existe')


# PROFESSOR
# nome = input('Digite seu primeiro nome: ')
# length = len(nome)
# if length > 1:
#     if length <= 4:
#         print('Seu nome é curto')
#     elif length >= 5 and length <= 6:
#         print('Seu nome é normal')
#     else:
#         print('Seu nome é muito grande')
# else:
#   print('Digite mais que uma letra')
