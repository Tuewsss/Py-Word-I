distancia_viagem = float(input("Digite a distância da viagem em km: "))
if distancia_viagem >= 200:
    preco_passagem = distancia_viagem * 0.45
else:
    preco_passagem = distancia_viagem * 0.50

print(f"O preço da passagem é R${preco_passagem:.2f}.")