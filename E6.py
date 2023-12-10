'''6. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de
quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os
dados do programa com as mensagens adequadas.'''



kilo = int(input("Quantos klos de peixe?"))
multa = 49
picles = 0

for x in range(multa + 1, kilo):
    picles +=4



print("Você pescou ", kilo, " kilos de peixe")

limite = kilo - 50

if kilo > 50:
    print("Infelizmente você pescou", limite, "kilos de peixe acima do limite, e terá que pagar", picles,"reais de multa")
else: print("você não passou do limite de 50kg de peixe, e não precisará pagar nenhuma multa")
