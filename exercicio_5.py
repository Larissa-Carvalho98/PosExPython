
### Exercício 5

cromossomo=input("Digite o cromossomo:")
posição=int(input("Digite a posição:"))
genoma=input("Digite o genoma de referência:")

if cromossomo == "chr17":
    print("Sim")
elif 41196312 <= posição <= 41277500 and genoma == "hg19":
    print("Sim")
elif 43044295 <=posição <= 43125483  and genoma == "hg38":
    print("Sim")
else:
    print("Não")