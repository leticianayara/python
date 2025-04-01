nome = input('Qual seu nome? ')
print(f'O seu nome é {nome=}')

#input vem sempre em str
numero_1 = input('Digite um número? ')
numero_2 = input('Digite outro número? ')
print(f'A soma dos números é: {numero_1 + numero_2}')

#ruim
numero_1 = float(input('Digite um número? '))
numero_2 = float(input('Digite outro número? '))
print(f'A soma dos números é: {numero_1 + numero_2}')

#boa
numero_1 = input('Digite um número? ')
numero_2 = input('Digite outro número? ')
float_numero_1 = float(numero_1)
float_numero_2 = float(numero_2)
print(f'A soma dos números é: {float_numero_1 + float_numero_2}')