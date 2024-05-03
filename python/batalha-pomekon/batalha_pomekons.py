import os

os.system('cls')

nomes = []
valoresDosGolpes = []

for count in range(1, 3):
    nomeInput = input(f'Nome do jogador {count}: ')
    nomes.append(nomeInput)

bonusInput = int(input('Bônus da partida: '))
os.system('cls')

for nome in nomes:
    print(f'{nome}, informe seus dados: ')
    ataque = int(input('Ataque: '))
    defesa = int(input('Defesa: '))
    nivel = int(input('Nível: '))

    if nivel % 2 != bonusInput:
        bonus = 0
    else:
        bonus = bonusInput

    valorGolpe = ((ataque + defesa) / 2) + bonus
    valoresDosGolpes.append(valorGolpe)
    os.system('cls')

if valoresDosGolpes[0] > valoresDosGolpes[1]:
    print(nomes[0], 'venceu o jogo')
elif valoresDosGolpes[0] < valoresDosGolpes[1]:
    print(nomes[1], 'venceu o jogo')
else:
    print('Empate')