#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido
#mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
#para o sindicato, faça um programa que nos dê:

#a. salário bruto.
#b. quanto pagou ao INSS.
#c. quanto pagou ao sindicato.
#d. o salário líquido.

hora = int(input('quanto vc recebe por hora'))

horasmes = int(input('quantas horas você trabalha por mes'))

salario = hora * horasmes

ir = 0.11 * salario
inss = 0.08 * salario
sindicato = 0.05 * salario
impostototal = ir + inss + sindicato
salario_liquido = salario - impostototal
print('Seu salário bruto é', salario)
print('voce pagou', inss, 'de INSS')
print('você pagou', sindicato, 'ao sindicato')
print('seu salario liquido é', salario_liquido)
