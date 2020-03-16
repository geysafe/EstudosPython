velocidade = int (input("Qual a velocidade do carro? R: "))

if velocidade>110:
    rapido = (velocidade-110)*5.00
    excedeu = velocidade-110
    print("Você foi multado, por exceder a velocidade em", excedeu,"Km do que é permitido")
    print("O valor da multa é de R$5,00 por Km excedido, então a sua multa é de R$", rapido)
else:
    print("Você é um motorista consciente e anda na velocidade permitida.")
