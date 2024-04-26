import os, random

def novaFase():
    os.system('cls')
    os.system('color 7')

def repostaCerta():
    os.system('cls')
    os.system('color 2')
    print('PARABENS! Você passou de fase')

def respostaErrada():
    os.system('cls')
    os.system('color 4')
    print('RESPOSTA ERRADA')
    print()

while True:

    # ABERTURA DO JOGO

    novaFase()

    print('''
    BEM VINDO À ILHA MALUCA
          ''')
    print('''
    Para desbloquear o tesouro escondido, você deve provar sua destreza. Resolva os
    desafios a seguir e siga as instruções para encontrar o caminho certo.
          ''')

    seguir = input('''
    Digite qualquer coisa para seguir ''')
    os.system('cls')

    print('Selecione a dificuldade do jogo: ')
    print('''
    (1) Fácil
    (2) Médio    
    (3) Difícil     
          
          ''')
    
    dificuldade = input('Sua escolha: ')

    if dificuldade == '2':
        numeroDeCocosInicial = random.randint(10, 30)
        cordaMetros = random.randint(11, 30)
        rioMetros = random.randint(5, 10)
        numeroPeriquitos = random.randint(10, 40)
    elif dificuldade == '3':
        numeroDeCocosInicial = random.randint(20, 50)
        cordaMetros = random.randint(21, 40)
        rioMetros = random.randint(15, 20)
        numeroPeriquitos = random.randint(20, 60)
    else:
        numeroDeCocosInicial = random.randint(4, 14)
        cordaMetros = random.randint(6, 15)
        rioMetros = random.randint(2, 5)
        numeroPeriquitos = random.randint(5, 10)


    # DESAFIO 1
    
    os.system('cls')

    print('''
    Você se depara com uma porta enorme guardada por um gigante adormecido. Para passar
    pela porta e continuar sua jornada, você precisa responder a seguinte questão:
    ''')

    print(f'''
    "Um macacos possui {numeroDeCocosInicial} cocos. Quantos cocos o macaco tem se eu pegar metade dos cocos que ele tem, mais dois cocos,
    e depois subtrair três cocos?"

    OBS: Cocos pela metade são jogados fora
    ''')

    cocosRespostaUser = int(input('''
    Resposta: '''))
    cocosRespostaCerta = ((numeroDeCocosInicial // 2) + 2) - 3

    if cocosRespostaUser == cocosRespostaCerta:
        repostaCerta()
        seguir = input('Digite qualquer coisa para seguir ')
    else:
        respostaErrada()
        escolha = input('Digite 1 para tentar novamente e 0 para fechar o jogo: ')
        if (escolha == '1'):
            continue
        else:
            quit()

    # DESAFIO 2
    
    novaFase()

    print('''
    Após passar pela porta, você entra em um labirinto infestado de
    crocodilos famintos. Para escapar deles, você precisa resolver o seguinte
    problema:
    ''')

    print(f'''
    "Se eu tenho uma corda de {cordaMetros} metros e preciso atravessar um rio de {rioMetros} metros de largura,
    quantos metros de corda a mais eu tenho para amarrar nas árvores e atravessar com
    segurança?"
    ''')

    metrosRespostaUser = int(input('''
    Resposta: '''))
    metrosRespostaCerta = cordaMetros - rioMetros

    if metrosRespostaCerta == metrosRespostaUser:
        repostaCerta()
        seguir = input('Digite qualquer coisa para seguir ')
    else:
        respostaErrada()
        escolha = input('Digite 1 para tentar novamente e 0 para fechar o jogo: ')
        if (escolha == '1'):
            continue
        else:
            quit()

    # DESAFIO 3

    novaFase()

    print('''
    Finalmente, você chega à câmara do tesouro, mas para abri-la, você precisa resolver um
    enigma final:
    ''')

    print(f'''
    "Se o número de tesouros enterrados na ilha é igual ao dobro do número de palmeiras,
    e o número de palmeiras é igual a três vezes o número de periquitos na ilha, e o número
    total de periquitos é {numeroPeriquitos}, quantos tesouros tem na ilha?"
    ''')

    tesourosRespostaUser = int(input('''
    Resposta: '''))
    tesourosRespostaCerta = (numeroPeriquitos * 3) * 2

    if tesourosRespostaUser == tesourosRespostaCerta:
        os.system('cls')
        os.system('color 2')
        print('PARABENS! Você zerou o jogo')
        verMapa = input('Digite qualquer coisa para revelar o mapa ')
        print("              ____        ")
        print("          .-'`    `'-.")
        print("       __/  __      __\__ ")
        print("    .-'  \ /  \    /  \  `-.")
        print("  .'       |   |  |   |      `.")
        print(" /    /`\  |   |  |   |  /`\   \ ")
        print("|     \__> |   |  | X | <__/    |")
        print(" \         |   |  |   |        /")
        print("  `.       |   |__|   |      .`")
        print("    `-.    \__/  \__/    .-`")
        print("       `'-..______..-'`")
        print()
        print('Jogo feito por João Pedro Pereira')
        print()
    else:
        respostaErrada()
        escolha = input('Digite 1 para tentar novamente e 0 para fechar o jogo: ')
        if (escolha == '1'):
            continue
        else:
            quit()
    break