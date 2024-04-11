####### FUNÇÕES #########
def mediaUnisinos(grauA, grauB):
    media = (grauA + 2* grauB) / 3.0
    return media


####### PROGRAMA PRINCIPAL #########


grauA = float(input("Digite sua média do grauA: "))
grauB = float(input("Digite sua média do grauB: "))


grauFinal = mediaUnisinos(grauA, grauB)
print("Grau final é ",grauFinal)