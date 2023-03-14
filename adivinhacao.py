import random
from time import sleep
import style

def jogar():
    style.purple('*' * 36)
    style.orange('{:^36}'.format('Bem vindo ao jogo de Adivinhação'))
    style.purple('*' * 36)

    num_secreto = random.randint(0, 100)
    tentativas = 0
    x = 0

    style.purple('=' * 20)
    print('''Níveis do jogo
    [1] \033[92mFácil\033[m
    [2] \033[93mMédio\033[m
    [3] \033[91mDifícil\033[m''')
    style.purple('=' * 20)

    dificuldade = int(input('Escolha a dificuldade do jogo: '))

    if dificuldade == 1:
        x = 12
        print('Escolhida a dificuldade \033[92mFácil\033[m.')
        sleep(1)
        print(f'Você tem {x} tentativas, boa sorte!')
    elif dificuldade == 2:
        x = 8
        print('Escolhida a dificuldade \033[93mMédio\033[m.')
        sleep(1)
        print(f'Você tem {x} tentativas, boa sorte!')
    elif dificuldade == 3:
        x = 5
        print('Escolhida a dificuldade \033[91mDifícil\033[m.')
        sleep(1)
        print(f'Você tem {x} tentativas, boa sorte!')

    for c in range (1, x+1):
        chute = int(input(f'Tentativa {c} de {x}: '))
        while True:
            if chute < 1 or chute > 100:
                print('Você digitou um número inválido, tente novamente.')
                chute = int(input('Digite um número: '))
            else:
                break
        tentativas += 1
        if chute < num_secreto:
            print('O número certo é\033[96m maior\033[m...')
            sleep(1.5)
        elif chute > num_secreto:
            print('O número secreto é\033[31m menor\033[m...')
            sleep(1.5)
        else:
            style.green('Parabéns! Você acertou!')
            style.green(f'Você precisou de {tentativas} tentativas para acertar.')
            sleep(1.5)
            break
        c += 1
        if c == x + 1:
            style.red(f'Você perdeu! O número correto era {num_secreto}.')
            sleep(1.5)
        elif c == x:
            style.red('ATENÇÃO! Esta é sua ÚLTIMA tentativa!')
            sleep(1.5)

    style.purple('*' * 32)
    style.orange('{:^32}'.format('FIM DO JOGO'))
    style.purple('*' * 32)
    sleep(1.5)

if __name__ == '__main__':
    jogar()