
import random
from time import sleep

computador = random.randint(0, 5) #Faz o computador embaralhar os números.
print('-=-' * 17)
print('Pensei em um número entre 0 e 5. Tente Adivinhar...') 
print('-=-' * 17)
jogador = int(input('Em que número pensei? ')) # A parte em que faz o jogador adivinhar.
print('\033[31mSORTEANDO UM NÚMERO!!!!.\033[m')
sleep(2)
if jogador == computador:
    print('Você acertou,Parabéns!!')   
else:     
    print(f'Eu ganhei! Pensei no número {computador} e não no {jogador}')