
### Exercício 7

frequencia_populacional=float(input("Digite a frequência da população em porcentagem:"))
gene=input("Digite um gene:").upper()
impacto=input("É alto ou baixo impacto?").upper()
reads=float(input("Quantidade de reads da variante:"))
vaf=float(input("Qual a frequência alélica da variante?"))     

if reads < 10  or vaf < 20:
    print('Não é relevante,pois deve ser um artefato!')
elif impacto == 'ALTO':
    if frequencia_populacional < 5 or gene in ['HFE','MEFV','GJB2']:
        print('A VARIANTE É RELEVANTE!')
    else:
        print('Não é relevante!')
else:
    print('Não é relevante!')