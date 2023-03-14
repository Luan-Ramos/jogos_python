import random
from time import sleep
import forca
import adivinhacao
import style

def escolher():
    while True:
        style.purple('*' * 36)
        style.orange('{:^36}'.format('Jogos Python'))
        style.purple('*' * 36)

        style.purple('=' * 20)
        print('''Escolha seu jogo:
        [1] \033[92mAdivinhação\033[m
        [2] \033[93mForca\033[m
        [3] \033[91mSair do Jogos Python\033[m''')
        style.purple('=' * 20)

        escolha = int(input('Digite a sua escolha: '))

        if escolha == 1:
            print('Você escolheu o jogo de \033[92mAdivinhação\033[m')
            sleep(1.5)
            adivinhacao.jogar()

        elif escolha == 2:
            print('Você escolheu o jogo de \033[93mForca\033[m')
            sleep(1.5)
            forca.jogar()

        elif escolha == 3:
            print('Você escolheu sair do Jogos Python, obrigado por jogar!')
            sleep(1.5)
            style.purple('*' * 32)
            style.orange('{:^32}'.format('FIM DO JOGO'))
            style.purple('*' * 32)
            break

if __name__ == '__main__':
    escolher()