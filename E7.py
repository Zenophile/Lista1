###7. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
#quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6
#metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
#galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem
#compradas e os respectivos preços em 3 situações:
#a. comprar apenas latas de 18 litros;
#b. comprar apenas galões de 3,6 litros;
###c. misturar latas e galões, de forma que o preço seja o menor.

import math

lata18 = 18
lata3 = 3.6

area = float(input("Quantos metros quadrados da área a ser pintada?"))

a = area / lata18
b = area / lata3
print(math.ceil(a))

print(math.ceil(b))

c = None


for latadezoito in range(0, int(area // 18) + 1):
    arearesto = area - latadezoito * 18
    latatres = arearesto / 3.6

    resultado = latadezoito * 80 * latatres *25

    c = (latadezoito, latatres)


round = tuple(round(x, 2) for x in c)

print(round)


