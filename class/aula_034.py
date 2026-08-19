salario = float(input("Digite o salário do funcionário: R$ "))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

print(f"O salário do funcionário era R${salario:.2f}. Com o aumento, o novo salário é R${salario + aumento:.2f}.")