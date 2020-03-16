minutos = float(input("Qual foi o consume em minutos: \n"))

if minutos < 200:
    conta = minutos * 0.20
elif minutos >= 200 and minutos <= 400:
    conta = minutos * 0.18
else:
    conta = minutos * 0.15

print("Sua conta é de R$", conta)