"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
        <- Contagem de complexidade (ruim)
"""
velocidade = 60 # velocidade atual do carro
local_carro = 100 # local em que oo carro esta na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 esta
RADAR_RANGE = 1 # A distancia onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 + RADAR_RANGE) or local_carro <= (LOCAL_1 - RADAR_RANGE) 

if carro_multado_radar_1 and vel_carro_pass_radar_1:
    print('Carro multado em radar')

elif vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar')