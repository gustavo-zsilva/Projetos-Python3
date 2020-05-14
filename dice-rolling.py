from random import choice
from time import sleep

print('\033[34mBem vindo ao randomizador de lados do dado!\033[m')

lados = [1,2,3,4,5,6]

placar = []
soma = 0

while len(placar) <= 5:

    rolar = str(input('\033[1;31mDigite algo para rolar o dado....\033[m '))
    print('Rolando...')
    lado_random = choice(lados)

    sleep(3)

    print(f'Você tirou o número {lado_random}!')
    print('Valor adicionado á sua tabela.')
    soma += lado_random
    placar.append(lado_random)

print(f'Seu placar foi : {placar}')
print(f'A soma total dos seus pontos é {soma}')





