import os

# FUNÇÕES
def checaPalavraChave():
    palavraEscondida = ''
    for letra in palavraChave:
            if letra in letrasEscolhidas:
                palavraEscondida += letra + ' '
            else:
                letra = '* '
                palavraEscondida += letra
    return palavraEscondida

##################################################

paraOuContinua = '1'
while paraOuContinua == '1':
    os.system('cls')
    desafiante = input('Nome do desafiante: ')
    competidor = input('Nome do competidor: ')

    os.system('cls')

    palavraChave = input('Palavra-chave: ').upper()
    
    dicas = []
    dicasSolicitadas = []
    letrasEscolhidas = []
    erros = 0
    vencedor = ''

    for contador in range(1, 4):
        dica = input(f'Dica {contador}: ').capitalize()
        dicas.append(dica)

    while True:
        menuEscolha = ''
        while menuEscolha != '0' and menuEscolha != '1' and menuEscolha != '2':
            os.system('cls')

            novaPalavra = checaPalavraChave()
            print(novaPalavra)
            print('----------------')

            if erros == 6 :
                vencedor = desafiante
                print(f'{desafiante} venceu o jogo!')
                print(f'A palavra era: {palavraChave}')
                menuEscolha = '0'
                break

            if '*' not in novaPalavra:
                vencedor = competidor
                print(f'{competidor} venceu o jogo!')
                menuEscolha = '0'
                break

            if erros != 0:
                print(f'Erros: {erros}')
                print()

            if len(dicasSolicitadas) > 0:
                for dica in dicasSolicitadas:
                    print(dica)
                print('----------------')

            print()
            print('(0) Sair')
            print('(1) Jogar')
            print('(2) Solicitar dica')
            menuEscolha = input('Sua escolha: ')
            print()
        
        if menuEscolha == '2':
            if len(dicas) > 0:
                print('DICA:', dicas[0])
                dicasSolicitadas.append(dicas[0])
                dicas.pop(0)
            else:
                print('Você já utilizou as 3 dicas')

            letraEscolhida = input('Digite uma letra: ').upper()
            letrasEscolhidas.append(letraEscolhida)
            if letraEscolhida not in palavraChave:
                erros += 1

        elif menuEscolha == '1':

            letraEscolhida = input('Digite uma letra: ').upper()
            letrasEscolhidas.append(letraEscolhida)
            if letraEscolhida not in palavraChave:
                erros += 1

        elif menuEscolha == '0':
            if not vencedor:
                os.system('cls')
            break
        
            
    print()
    print('(0) Sair do jogo')
    print('(1) Jogar novamente')
    paraOuContinua = input('Sua escolha: ')