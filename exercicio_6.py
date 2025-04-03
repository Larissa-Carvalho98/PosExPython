
### Exercício 6

viagem =str(input("Qual o país que você vai viajar?").upper()).strip()
reais=float(input("Quantos reais você quer converter?"))

USD= reais / 5
ARS= reais * 180
JPY= reais * 30

if viagem == "ESTADOS UNIDOS" :
    print("{} USD".format(USD))
elif viagem == "ARGENTINA":
    print("{} ARS".format(ARS))
elif viagem == "JAPÃO":
    print("{} JPY".format(JPY))
else:
    print("Não temos essa moeda em caixa,desculpe!")
