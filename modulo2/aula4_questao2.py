#2 - Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. 
#Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:
#86 graus Fahrenheit são 30 graus Celsius.

F = int(input("Digite a temperatura wm Fahrenheit: "))
C = (F - 32) * (5/9)
print(f"{F} graus Fahrenheit são {C:.2f} graus Celsius.")