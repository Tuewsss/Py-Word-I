velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade > 80:
    print("Você ultrapassou o limite de velocidade! MULTADO!")
    multa = (velocidade - 80) * 7
    print(f"Você deve pagar uma multa de R${multa:.2f}.")
else:
    print("Você está dentro do limite de velocidade. Dirija com segurança!")