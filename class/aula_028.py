import random

iniciar = input("Deseja iniciar o jogo? [S/N] ").strip().upper()[0]

if iniciar == "S":
    print("Estou pensando em um número entre 1 e 5. Tente adivinhar!")
    numero_pensado = random.randint(1, 5)
    tentativa = int(input("Tente adivinhar o número que estou pensando (entre 1 e 5): "))
    if tentativa != numero_pensado:
        print(f"Você errou! O número que eu estava pensando era {numero_pensado}.")
    else:
        print("Você acertou! Parabéns!")
else:
    print("Jogo encerrado.")

