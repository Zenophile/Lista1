#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a
#temperatura em graus Celsius. C = (5 * (F-32) / 9).

farenheit = int(input("Quantos graus em farenheit?"))
celsius = 5 * (farenheit-32) / 9

print("A temperatura em Celsius é", celsius)
