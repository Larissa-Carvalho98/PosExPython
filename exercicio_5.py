
### Exercício 5

cromossomo=input("Digite o cromossomo:").strip()
posição=int(input("Digite a posição:"))
genoma=input("Digite o genoma de referência:").strip()

if cromossomo == "chr17" and genoma == "hg19" and 41196312 < posição < 41277500 :
    print("Sim")
elif cromossomo == "chr17" and genoma == "hg38" and 43044295 < posição < 43125483 : 
    print("Sim")
else:
    print("Não")