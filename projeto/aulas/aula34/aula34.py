"""
Repetição
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um codigo não tem fim
"""
# Loop infinito
# condicao= True

# while condicao:
#     nome = input('Digite seu nome: ')
#     print(f'Seu nome é {nome}')

# print('Acabou')

condicao= True

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')