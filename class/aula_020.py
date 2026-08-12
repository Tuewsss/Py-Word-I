import random
aluno1 = "Mateus"
aluno2 = "Rina"
aluno3 = "Rikelmy"
aluno4 = "Marcu"
ordem = random.sample([aluno1, aluno2, aluno3, aluno4], 4)
print(f"A ordem de apresentação dos alunos será: {ordem[0]}, {ordem[1]}, {ordem[2]}, {ordem[3]}")