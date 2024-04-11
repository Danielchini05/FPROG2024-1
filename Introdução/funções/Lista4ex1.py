######## Funções ########
def cumprimentar(nome):
    print("Olá, ",nome,"!")



######3# Programa Principal #########


nome1 = input("Usuário1, Digite seu nome: ")
cumprimentar(nome1)

nome2 = input("Usuário 2, Digite seu nome: ")
cumprimentar(nome2)

for i in range(5):
    print("Usuário", i+1, end = "")
    nome = input(", digite seu nome: ")
    cumprimentar(nome2)