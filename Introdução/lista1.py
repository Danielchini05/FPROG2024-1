# # fundamentosDaProgramacao
# Comandos de Entrada/Saída e Variáveis
# 1. Utilizando o OnlineGDB, pesquise e implemente um programa que escreva na tela “Olá
# Mundo!” em 3 linguagens de programação diferentes. Qual é o comando de saída de
# dados nestas 3 linguagens?

# Python:
# print ('Hello World')

# Java:
# 	public class Main
# 	{
# 		public static void main(String[] args) {
# 			System.out.println("Hello World");
# 		}
# 	}

# C:
# 	int main()
# 	{
# 	    printf("Hello World");
	
# 	    return 0;
# 	}


# 3. Escreva um programa em linguagem Python que solicite o nome do usuário e, em seguida,
# imprima uma mensagem de boas-vindas na tela, utilizando o nome fornecido.

nome = input('Digite seu nome: ')
print('Olá, ',nome,'!!!')


# nome_do_usuario = input("Qual o seu nome?")

# print("Boas vindas, ",nome_do_usuario)

# 4. Escreva um programa em Python que realize o seguinte procedimento:
#   a. Imprima na tela a seguinte questão: Qual é o verdadeiro nome do super-herói
#   Batman?
#   b. Apresente cinco alternativas para o usuário, cada uma em uma linha: a) Bruce
#   Wayne b) Clark Kent c) Peter Parker d) Tony Stark e) Steve Rogers
#   c. Armazene a letra correspondente à resposta correta (‘a’) em uma variável.
#   d. Solicite ao usuário que digite sua resposta, e a armazene em uma variável.
#   e. Ao final, o programa deve exibir na tela a resposta do usuário e a resposta correta.
#   Por exemplo, se o usuário digitou como resposta a alternativa ‘d’, a mensagem
#   seria esta:
#   Você respondeu alternativa d. A resposta correta é a alternativa a.
# 5. Como poderíamos tornar o programa acima mais genérico, de maneira que pudéssemos
# registrar qualquer questão objetiva com 5 alternativas?
