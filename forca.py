import random
from time import sleep
import style


def jogar():
    inicio()
    palavra = escolha_palavra()


    letras_certas = ['_'] * len(palavra)
    enforcou = False
    acertou = False
    erros = 0
    print(letras_certas)
    letras_usadas = []

    while not enforcou and not acertou:
        chute = input('Digite uma letra: ')[0].strip().upper()
        while True:
            if chute in letras_usadas:
                chute = input('\033[93mEsta letra já foi usada, tente novamente: \033[m')[0].strip().upper()
            else:
                break
        if chute in palavra:
            chute_correto(chute, palavra, letras_certas)
        else:
            erros += 1
            desenha_forca(erros)
            if erros < 6:
                style.yellow(f'Você errou e ainda tem {7 - erros} tentativas!')
            elif erros == 6:
                style.red('Você pode errar apenas mais 1 vez, escolha com cuidado!')
        letras_usadas.append(chute)
        style.lightcyan(f'Letras utilidazadas: {letras_usadas}')
        if erros == 7:
            perdeu(palavra)
            enforcou = True
        elif '_' not in letras_certas:
            venceu()
            acertou = True
        print(letras_certas)
        sleep(0.5)

    final()


def inicio():
    style.purple('*' * 36)
    style.orange('{:^36}'.format('Bem vindo ao jogo de Forca'))
    style.purple('*' * 36)


def escolha_palavra():
    arquivo = open('palavras.txt', 'r')
    palavras_jogo = []
    for linha in arquivo:
        palavras_jogo.append(linha.strip().upper())
    arquivo.close()
    palavra = random.choice(palavras_jogo)
    return palavra


def chute_correto(chute, palavra, letras_certas):
    index = 0
    for letra in palavra:
        if chute == letra:
            letras_certas[index] = letra
        index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |       |     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def perdeu(palavra):
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    style.red('Você errou 7 vezes e foi enforcado!')
    style.red(f'A palavra correta era {palavra}')


def venceu():
    style.green('Você acertou a palavra e venceu o jogo!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def final():
    style.purple('*' * 32)
    style.orange('{:^32}'.format('FIM DO JOGO'))
    style.purple('*' * 32)
    sleep(1.5)


if __name__ == '__main__':
    jogar()
