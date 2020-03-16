minutos = float(input("Qual foi o consume em minutos: \n"))

if minutos < 200:
    conta = minutos * 0.20
else:
    if minutos <= 400:
        conta = minutos * 0.18
    else:
        if minutos <= 800:
            conta = minutos * 0.15
        else:
            conta = minutos * 0.08

print("Sua conta é de R$", conta)

''' 
aprendendo a usar ESTRUTURAS ANINHADAS
inclusão da tarifa promocional $0,08 acima de 800 minutos
'''