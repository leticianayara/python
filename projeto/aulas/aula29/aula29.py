"""
Introdução ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o numero que vc digitar: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:',numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')     
except:
    print('Isso não é um numero inteiro')

# if (numero_str.isdigit()):
#     numero_float = int(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')                   
# else:
#     print('Isso não é um numero inteiro')

