velocidade_maxima=80
multa_por_quilometro=7

velocidade_carro= float(input("Qual a sua velocidade?"))

if velocidade_carro > velocidade_maxima:
    multa=(velocidade_carro-velocidade_maxima)* multa_por_quilometro
    print('Você foi multado, o valor é R${}!!'.format(multa))
print("Tenha um bom dia!!")
