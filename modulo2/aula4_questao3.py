#3 - Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado
#  ltiplicanmudo a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:
#Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito)
#A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).
produto1 = str(input("Digite o nome do produto 1: "))
preco1 = float(input("Digite o preço unitário do produto 1: "))
quantidade1 = int(input("Digite a quantidade do produto 1: "))
total1 = preco1 * quantidade1
produto2 = str(input("Digite o nome do produto 2: "))
preco2 = float(input("Digite o preço unitário do produto 2: "))
quantidade2 = int(input("Digite a quantidade do produto 2: "))
total2 = preco2 * quantidade2
produto3 = str(input("Digite o nome do produto 3: "))
preco3 = float(input("Digite o preço unitário do produto 3: "))
quantidade3 = int(input("Digite a quantidade do produto 3: "))
total3 = preco3 * quantidade3
total_final = total1 + total2 + total3
print(f"Total: R${total_final: ,.2f}")

