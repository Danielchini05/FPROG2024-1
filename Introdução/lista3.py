# Escreva um programa que leia dois números e efetue uma divisão, mas somente se o divisor for
# diferente de zero; quando isto ocorrer, é mostrada uma mensagem de erro apropriada.


# dividendo = float(input("Digite o dividendo: "))
# divisor = float(input("Digite o divisor: "))

# if divisor != 0:
#     resultado = dividendo / divisor 
#     print(f"O resultado é {resultado}")

#     else:
#     print("O divisor não pode ser zero!")


# Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que A
# + C.

# var_a = float(input("Digite o valor a: "))
# var_b = float(input("Digite o valor b: "))
# var_c = float(input("Digite o valor c: "))

# if var_a + var_b > var_a + var_c:
#     print("A soma do valor a e b é maior do que a soma a e c")
    
# else:
#     print("A soma a e b é menor do que a soma a e c")


# Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo
# o resultado.

# numero = float(input("Digite um número: "))

# if numero > 0:
#     dobro = numero * 2
#     print(f"O dobro do número é {dobro}.")

# else: 
#     triplo = numero * 3
#     print(f"O triplo do número é {triplo}.")



# # Crie um programa que verifica se um número inteiro informado pelo usuário é divisível por 3

# numero = float(input("Digite um número para saber se ele é divisísivel por 3: "))

# if numero % 3 == 0:
#     print("O número é divisível por 3")

# else: 
#     print("O número não é dívisivel por 3")


# Faça um algoritmo para receber um número qualquer do usuário e informar na tela se é par ou se
# é ímpar.

# numero = float(input("Digite um número "))

# if numero % 2 == 0:
#     print("O numero é par")

# else:
#     print('O número é impar')


# Brincadeira do PAR ou ÍMPAR. Pergunte para o usuário se ele aposta em PAR ou ÍMPAR. Depois
# disso, peça para ele digitar um número de 0 a 5 (como se fosse mostrar os dedos da mão. Sorteie
# um número de 0 a 5 e some com o que o usuário digitou. Se o usuário escolheu PAR e o valor da
# soma for par OU se ele escolheu ÍMPAR e o valor da soma é ímpar, diga que ele venceu. Senão, diga
# que o programa venceu

# import random

# jogador1 = input("Escolha par ou ímpar: ").lower()

# if jogador1 == 'par':
#     jogador2 = 'ímpar'
# else:
#     jogador2 = 'par'

# num_jogador1 = int(input("Insira um número de 0 a 5: "))
# num_jogador2 = random.randint(0, 5)

# soma = num_jogador1 + num_jogador2

# print(f"O jogador 2 escolheu: {num_jogador2}")
# print(f"A soma dos números é: {soma}")

# if (soma % 2 == 0 and jogador1 == 'par') or (soma % 2 != 0 and jogador1 == 'ímpar'):
#     print("Jogador 1 venceu")
# else:
#     print("Jogador 2 venceu")





