"""
Interpolação básica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Leticia'
preco = 1000.95897643
variavel = '%s, o preco total foi R$%.2f' %(nome, preco)
print(variavel)


print('O hexadecimal de %d é %x' %(1500, 1500))
print('O hexadecimal de %d é %04x' %(1500, 1500))
print('O hexadecimal de %d é %08X' %(1500, 1500))