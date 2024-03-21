# 1. Faça um algoritmo que leia uma quantidade de tempo em minutos e escreva o tempo equivalente
# em segundos na tela.

# minutos = int(input("Escreva o tempo em minutos:"))

# segundos = minutos * 60

# print(f"{minutos} minutos equivalem a {segundos}segundos")


# 2. Um turista deseja comprar dólares em uma casa de câmbio. Escreva um programa que leia a
# cotação do dólar para real, a quantidade de dólares que o turista deseja comprar, e calcule o valor
# total em reais que ele precisará pagar.

# cotacao_dolar = float(input("Digite a cotação do dólar em reais: "))
# quantidade_dolar = float(input("Digite a quantidade de délar que deseja comprar: "))

# quantidade_real = quantidade_dolar + cotacao_dolar

# print(f"{quantidade_dolar} dólares equivalem a {quantidade_real:.2f} reais.")

# 3. Um restaurante de buffet a quilo cobra R$ 40,00 por quilo. Escreva um programa que leia o peso
# do prato do cliente e calcule o valor a ser pago.

# preco_quilo = 40

# peso_prato = float(input("Digite o peso do seu prato em quilos: "))

# valor_a_pagar = preco_quilo * peso_prato

# print(f"O valor a ser pago pelo seu prato é de R$ {valor_a_pagar:.2f}.")


# 4. Faça um algoritmo que permita ao aluno calcular a sua média final na Unisinos. Leia a nota do grau
# A e do grau B e escreva o resultado na tela. Lembrando que o Grau A vale 1/3 e o Grau B 2/3.

# nota_grau_a = float(input("Digite a nota do grau A: "))
# nota_grau_b = float(input("Digite a nota do grau B: "))


# media_final = (nota_grau_a * 1/3) + (nota_grau_b * 2/3)

# print(f"A média final do aluno é: {media_final:.2f}")


# 5. Um motorista deseja encher o tanque do seu carro com gasolina. Escreva um algoritmo para ler o
# preço do litro da gasolina e o valor que o motorista tem disponível para abastecer. Calcule quantos
# litros ele conseguiu colocar no tanque e exiba na tela.

# preco_litro_gasolina = float(input("Digite o preço do litro da gasolina: "))
# valor_disponivel = float(int("Digite o valor disponível para abastecer: "))

# litros_abastecidos = valor_disponivel / preco_litro_gasolina

# print(f"O motorista conseguiu colocar {litros_abastecidos:.2f} litros no tanque.")

# 6. A loja de eletrônicos TechMundo vende uma certa quantidade de smartphones e uma quantidade
# de tablets a cada dia. Cada smartphone custa R$ 1000,00 e cada tablet custa R$ 1500,00. Ao final
# do dia, o dono quer saber quanto arrecadou com a venda dos smartphones e dos tablets. Escreva
# um programa que leia o número de smartphones e tablets vendidos em um dia e calcule o total
# arrecadado.

# preco_smartfone = 1000.00
# preco_table = 1500.00

# num_smartphones = int(input("Digite o número de smartfones vendidos: "))
# num_tablets = int(input("Digite o número de tablets vendidos: "))

# total_smartphones = num_smartphones * preco_smartfone
# total_tablets = num_tablets * preco_table
# total_arrecadado = total_smartphones + total_tablets

# print(f"Total arrecadado com a venda de smartphones: R${total_smartphones:.2f}")
# print(f"Total arrecadado com a venda de tablets: R$ {total_tablets:.2f}")
# print(f"Total arrecadado no dia: R$ {total_arrecadado:.2f}")

# 7. Um criador de pássaros deseja saber a quantidade de ração diária necessária para alimentar seus
# pássaros. Cada pássaro consome 30 gramas de ração por dia. Escreva um programa que leia o
# número de pássaros que o criador possui e calcule a quantidade total de ração necessária por dia.

# racao_por_passaro = 30

# num_passaros = int(input("Digite o número de pássaros que você possui: "))

# quantidade_total_racao = num_passaros * racao_por_passaro

# print(f"A quantidade total de ração necessária por dia é de {quantidade_total_racao} gramas")

# 8. Um usuário deseja converter a temperatura de Celsius para Fahrenheit. Escreva um programa que
# leia a temperatura em Celsius e exiba a temperatura equivalente em Fahrenheit.

# temperatura_celcius = float(input("Digite a temperatura em Celsius: "))

# temperatura_fahrenheit = (temperatura_celcius * 9/5) + 32

# print(f"A temperatura equivalente em Fahrenheit é: {temperatura_fahrenheit:.2f}°F")



# 9. Durante uma liquidação uma loja resolveu dar quinze por cento de desconto nas compras feitas
# pelos clientes. Faça um programa que leia o valor da compra e escreva o valor da compra com o
# desconto.

# valor_compra = float(input("Digite o valor da compra: "))

# desconto = valor_compra * 0.15

# valor_com_desconto = valor_compra - desconto

# print(f"O valor da compra com desconto é: R$ {valor_com_desconto:.2f}")

# 10. O lojista gostou tanto do seu programa anterior que encomendou outro. Dessa vez ele quer que
# você calcule quanto cada cliente gastou na loja apenas informando o número de camisetas, calças
# e cintos comprados. As camisetas custam R$ 25,00, as calças cem reais e os cintos 40 reais. Some o
# valor da compra e ao final dê um desconto de 10 por cento sobre o total. Exiba na tela o valor do
# desconto e o valor da compra.

preco_camiseta = 25.00
preco_calca = 100.00
preco_cinto = 40.00

num_camisetas = int(input("Digite o número de camisetas compradas: "))
num_calcas = int(input("Digite o número de calcas compradas: "))
num_cintos = int(input("Digite o número de cintos compradas: "))


total_sem_desconto = (num_camisetas * preco_camiseta) + (num_calcas * preco_calca) + (num_cintos * preco_cinto)

desconto = total_sem_desconto * 0.10

total_com_desconto = total_sem_desconto - desconto

print(f"O valor do desconto é R$ {desconto:.2f}")
print(f"O valor da compra com desconto é: R$ {total_com_desconto:.2f}")
