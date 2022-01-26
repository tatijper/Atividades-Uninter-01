fase01 = ['*', '*', '_', 'G', 'R', '_', '*', '*']
gabarito01 = ['*', '*', 'G', 'G', 'R', 'R', '*', '*']
fase02 = ['_', '*', '*', '*', '*', 'C', '_', '_']
gabarito02 = ['O', '*', '*', '*', '*', 'C', 'C', 'C']
fase03 = ['_', '*', '*', '*', '_', 'G', '_', '*']
gabarito03 = ['R', '*', '*', '*', 'O', 'G', 'G', '*']
fase04 = ['_', '_', '_', '*', '*', 'R', '*', '*']
gabarito04 = ['Q', 'O', 'Q', '*', '*', 'R', '*', '*']
endgame = False

print('HOTEL DOS ANIMAIS')
print('Quartos')
print('[1,2,3,4]')
print('[5,6,7,8]')
print('Bem vindo a fase 1!')
print('Escolha um dos quartos para acomodar o gato e o rato.')
print('Quartos disponiveis 3 e 6.')
print('Lembrando que espaços com * não estão disponíveis!')

print(fase01[0:4])
print(fase01[4:8])


posicao01 = int(input('Escolha um quarto para alocar o gato: '))
if fase01[int(posicao01) - 1] == '_':
    fase01[int(posicao01) - 1] = 'G'


posicao02 = int(input('Escolha um quarto para alocar o rato: '))
if fase01[int(posicao02)-1] == '_':
    fase01[int(posicao02)-1] = 'R'

for i in range(0, len(fase01)):
    if fase01[i] == gabarito01[i]:
        continue

    else:
        endgame = True
        print('Voce perdeu!!')
        break

if endgame == False:
    print('Bem vindo a fase 2!')
    print('Escolha um dos quartos para acomodar o cão, o cão e o osso.')
    print('Quartos disponiveis 1, 7 e 8.')

    print(fase02[0:4])
    print(fase02[4:8])

    posicao03 = int(input('Escolha um quarto para alocar o cão: '))
    if fase02[int(posicao03) - 1] == '_':
        fase02[int(posicao03) - 1] = 'C'


    posicao04 = int(input('Escolha um quarto para alocar o cão: '))
    if fase02[int(posicao04)-1] == '_':
        fase02[int(posicao04)-1] = 'C'

    posicao05 = int(input('Escolha um quarto para alocar o osso: '))
    if fase02[int(posicao05)-1] == '_':
        fase02[int(posicao05)-1] = 'O'

    for i in range(0, len(fase02)):
        if fase02[i] == gabarito02[i]:
            continue
        else:
            endgame = True
            print('Voce perdeu!!')
        break
if endgame == False:
    print('Bem vindo a fase 3!')
    print('Escolha um dos quartos para acomodar o gato, rato, e osso.')
    print('Quartos disponiveis 1, 5 e 7.')

    print(fase03[0:4])
    print(fase03[4:8])

    posicao06 = int(input('Escolha um quarto para alocar o gato: '))
    if fase03[int(posicao06) - 1] == '_':
        fase03[int(posicao06) - 1] = 'G'

    posicao07 = int(input('Escolha um quarto para alocar o rato: '))
    if fase03[int(posicao07)-1] == '_':
        fase03[int(posicao07)-1] = 'R'

    posicao08 = int(input('Escolha um quarto para alocar o osso: '))
    if fase03[int(posicao08)-1] == '_':
        fase03[int(posicao08)-1] = 'O'

    for i in range(0, len(fase03)):
        if fase03[i] == gabarito03[i]:

            continue
        else:
            endgame = True
            print('Voce perdeu!!')
        break

if endgame == False:

    print('Bem vindo a fase 4!')
    print('Escolha um dos quartos para acomodar o queijo, queijo, e osso.')
    print('Quartos disponiveis 1, 2 e 3.')

    print(fase04[0:4])
    print(fase04[4:8])

    posicao09 = int(input('Escolha um quarto para alocar o queijo: '))
    if fase04[int(posicao09) - 1] == '_':
        fase04[int(posicao09) - 1] = 'Q'


    posicao10 = int(input('Escolha um quarto para alocar o queijo: '))
    if fase04[int(posicao10)-1] == '_':
        fase04[int(posicao10)-1] = 'Q'

    posicao11 = int(input('Escolha um quarto para alocar o osso: '))
    if fase04[int(posicao11)-1] == '_':
        fase04[int(posicao11)-1] = 'O'

    for i in range(0, len(fase04)):
        if fase04[i] == gabarito04[i]:

            continue
        else:
            endgame = True
            print('Voce perdeu!!')
        break
    print('Voce ganhou o jogo!!', '\n', 'Parabens!!!!')
