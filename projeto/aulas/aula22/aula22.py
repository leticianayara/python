# Operadores logicos
# and (e) or (ou) not (nao)
# and - todas as condições precisam ser
# verdadeiras.
# se qq valor for considerado falso,
# a expressao inteira sera avaliada naquele valor
# são consideradas falsy (que vc ja viu)
#   0, 0.0, '', False
# Tambem existe o tipo None que é
# usado para representar um nao valor

entrada = input('[E]ntrar [S]air: ')
senha_permidica = '123456'

if entrada == 'E' or entrada == 'e':
   senha_digitada = input('Senha: ')
   if(senha_digitada == senha_permidica):
       print('Entrar')
   else:
       print('Acesso negado')
else:
   print('Sair')

# Avaliação de curto circuito
print(True or True or True)
print(True or False or True)
