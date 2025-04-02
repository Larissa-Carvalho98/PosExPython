
### Exercício 6

viagem =str(input("Qual o país que você vai viajar?")).strip() .capitalize()
reais=float(input("Quantos reais você quer converter?"))

USD= reais / 5
ARS= reais * 180
JPY= reais * 30

if viagem == "Estados Unidos,Japão,Argentina" :
    print("Quantos reais você quer converter?")
elif viagem == "Estados Unidos" :
    print("{} USD".format(USD))
elif viagem == "Argentina":
    print("{} ARS".format(ARS))
elif viagem == "Japão":
    print("{} JPY".format(JPY))
else:
    print("Não temos essa moeda em caixa,desculpe!")
