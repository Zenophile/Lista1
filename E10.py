#10. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os
#valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é:
#equilátero, isósceles ou escaleno.

lado1 = int(input("informe o primeiro lado do triangulo"))
lado2 = int(input("informe o segundo lado do triangulo"))
lado3 = int(input("informe o terceiro lado do triângulo"))
print("informe o quarto lado do triangulo")
print("Bobinho, triangulos tem apenas 3 lados, agora vamos para os resultados...\n\n")

if lado1 == lado2 and lado2 == lado3:
    print("os lados formaram um triangulo equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Os lados formaram um triângulo isóceles")
else:
    print("Os lados formaram um triângulo Escaleno")
