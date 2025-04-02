"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

# string = 'Leticia Costa'
# #outra_variavel = string
# string[3] = 'ABC'
# print(string[3])

string = 'Leticia Costa'
outra_variavel = f'{string[:3]}'
print(outra_variavel)

print('-' * 15)

string = 'Leticia Costa'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
print(string.capitalize())

print('-' * 15)

print(string.zfill(100))