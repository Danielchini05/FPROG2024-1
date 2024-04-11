######## FUNÇÕES #######
def musicaElefantes(n):
    for i in range(1, n):
        print(i, "elefantes(s) incomoda(m) muita gente,")
        print(i+1, "elefantes(s) ", end="")
        for j in range(0, i+1):
            print("incomodam, ", end="")
        print("muito mais!")


######## PROGRAMA PRINCIPAL ########

musicaElefantes()