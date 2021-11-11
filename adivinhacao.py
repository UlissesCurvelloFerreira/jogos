import random

def jogar():

    print('********************************')
    print('Bem-vindo ao jogo de adivinhação')
    print('********************************')

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual o nível de difículdade')
    print('(1)fácil (2)médio (3)difícil')
    nível = int(input('define o nível'))

    if(nível == 1):
        total_de_tentativas = 20

    elif(nível == 2):
        total_de_tentativas = 10

    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print('tentativas: {} de {}'. format(rodada, total_de_tentativas))
        chute = input('digite um número entre 1 e 100:')
        print('você digitou', chute)
        chute = int(chute)

        if(chute < 1 or chute > 100):
            print('você deve digitar um número entre 1 e 100')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print('você acertou e fez a {} pontos'.format(pontos))
            break
        else:
            if(maior):
                print('você errou! Seu número chutado foi maior que o némero secreto')
            elif(menor):
                print('você errou! Seu número chutado foi menor que o número secreto')
            pontos_perdidos = abs(chute - numero_secreto)
            pontos = pontos - pontos_perdidos

    print('FIM DE JOGO')
if(__name__ == "__main__"):
    jogar()