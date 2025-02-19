"""

CONSTANTE = 'Variaveis' que não vão mudar
Muitas condições no mesmo if(ruim
    <- Contagem de complexidade (ruim)
"""

velocidade = 61 #KM
local_carro = 100 #KM

RADAR_1 = 60 #KM
LOCAL_1 = 100 #KM
RADAR_RANGE = 1 #KM

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('A velocidade do carro passou do radar!')

if carro_passou_radar_1:
    print('CARRO PASSOU RADAR 1')

if carro_passou_radar_1:
    print('CARRO MULTADO EM RADAR 1')