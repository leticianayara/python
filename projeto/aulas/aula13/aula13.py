nome = 'Leticia Costa'
altura = 1.48
peso = 55
imc = ...   # peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso:.3f} quilos e seu IMCC é'
imc = peso / (altura * altura)
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)


# Leticia Costa tem 1.48 de altura,
# pesa 55 quilos e seu IMC é 
#  25.109569028487