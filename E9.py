'''
9. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa
que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante: aumento de 5%
Após o aumento ser realizado, informe na tela:
a. o salário antes do reajuste;
b. o percentual de aumento aplicado;
c. o valor do aumento;
d. o novo salário, após o aumento.
'''



print("Reajuste de salários")
vinteporcento = 1.2
quinzeporcento = 1.15
dezporcento = 1.10
cincoporcento = 1.05
salario1 = int(input(print("Digite o Salário do Colaborador")))
salarioantes = salario1
if salario1 <= 280:
    salario1 = salario1 * vinteporcento
    print("O salario de R$",salarioantes, "Recebeu um ajuste de ", vinteporcento, "e agora é R$",salario1)
elif salario1 > 280 and salario1 < 700:
    salario1 = salario1 * quinzeporcento
    print("O salario de R$",salarioantes, "Recebeu um ajuste de ", quinzeporcento, "e agora é R$",salario1)
elif salario1 > 700 and  salario1 < 1500:
    salario1 = salario1 * dezporcento
    print("O salario de R$",salarioantes, "Recebeu um ajuste de ", dezporcento, "e agora é R$",salario1)

else:
    salario1 = salario1 * cincoporcento
    print("O salario de R$",salarioantes, "Recebeu um ajuste de ", cincoporcento, "e agora é R$",salario1)





