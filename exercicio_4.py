
### Exercício 4

cromossomo=input("Digite o cromossomo:")
posição=int(input("Digite a posição:"))

if cromossomo == "chr17":
    print("Sim")
elif 41196312 <= posição <= 41277500:
    print("Sim")
else:
    print("Não")