reta_1 = float(input("Digite o comprimento da reta: "))
reta_2 = float(input("Digite o comprimento da reta: "))
reta_3 = float(input("Digite o comprimento da reta: "))

if reta_1 + reta_2 > reta_3 and reta_1 + reta_3 > reta_2 and reta_2 + reta_3 > reta_1:
    print("As retas podem formar um triângulo.")
else:
    print("As retas não podem formar um triângulo.")
