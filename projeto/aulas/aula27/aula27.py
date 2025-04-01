"""
Fatiamento de strings
 012345678
 Olá Mundo
-987654321

Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caaracteres da str
"""
variavel = 'Olá Mundo'
print(variavel[5])
print(variavel[-4])
print(variavel[4:8])
print(variavel[4:])
print(variavel[0:5])
print(variavel[:5])

print(len(variavel[4:]))
print(variavel[0:len(variavel):1])
print(variavel[0:len(variavel):2])
print(variavel[0:len(variavel):-2])
print(variavel[-1:-len(variavel):-2])