# Operadores in e not in
# Strings são iteraveis
#  0 1 2 3 4 5
#  O t a v i o
# -6-5-4-3-2-1

# nome = 'Leticia'

# print(nome[2])
# print(nome[-4])
# print('cia' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('cia' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')