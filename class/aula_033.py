numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))

if numero_1 >= numero_2 and numero_1 >= numero_3:
    maior = numero_1
    if numero_2 <= numero_1 and numero_2 <= numero_3:
        menor = numero_2
    else:
        menor = numero_3
elif numero_2 >= numero_1 and numero_2 >= numero_3:
    maior = numero_2
    if numero_1 <= numero_2 and numero_1 <= numero_3:
        menor = numero_1
    else:
        menor = numero_3
else:
    maior = numero_3
    if numero_1 <= numero_3 and numero_1 <= numero_2:
        menor = numero_1
    else:
        menor = numero_2

print(f"O maior número é {maior} e o menor é {menor}.")