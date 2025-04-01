"""
Formatacao basica de strings
s - string
d - int
f - float
.<numero de digitos>f - float formatado
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - Centro
= - forca o numero a aparecer depois do zeros
+ ou - -> Sinal

Ex. 0 > -100.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.48085340524239: .1f}.')
print(f'{1000.48085340524239:0=+10,.1f}.')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
print(f'{variavel!s}')
print(f'{variavel!a}')