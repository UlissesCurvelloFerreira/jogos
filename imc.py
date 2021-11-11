def calcula_imc():

    nome = input('Qual é seu nome')
    peso = float(input('Qual é seu peso?'))
    altura = float(input('Qual é sua altura?'))

    calcula_imc = peso / (altura * altura)

    if calcula_imc < 18.5:
        print(f'Seu IMC é de {round(calcula_imc, 2)} \nvocê está abaixo do peso')

    elif calcula_imc < 24.9:
        print(f'Seu IMC é de {round(calcula_imc, 2)} \nvocê está com o peso ideal ideal parabéns')

    elif calcula_imc < 29.9:
        print(f'Seu IMC é de {round(calcula_imc, 2)} \nvocê está levemente acima do peso')

    elif calcula_imc < 34.9:
        print(f'Seu IMC é de {round(calcula_imc, 2)} \nvocê está com obesidade grau I')

    elif calcula_imc < 40:
        print(f'Seu IMC é de {round(calcula_imc, 2)} \nvocê está com obesidade grau II severa')

    else:
        print(f'Seu IMC é de {round(calcula_imc, 2)} \nvocê está com obesidade garu III mórbida (cuidado!!!)')

    return print(f'Seu imc é de {round(calcula_imc,2)} \n' )


calcula_imc()
