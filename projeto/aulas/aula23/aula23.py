# Operador logico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:  
    print('Senha nao digitada.')


print(not False) # True
print(not True) # False