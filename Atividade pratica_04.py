from random import seed
from random import randint
seed(100)
aleatorio = randint(100, 400)
cadastro = {'nome': [], 'email': [], 'telefone': [], 'curso': [], 'voucher': []}
encerrar = False

print('********Programa de vouchers para aulas de Python********')
while encerrar == False:

    print("******MENU******")
    print("1 - Cadastrar aluno")
    print("2 - Visualizar inscrições")
    print("3 - Sair")
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print('***Opção', opcao, ': Novo Cadastro***')

        for i in range(1):
            nome = input('Digite o nome completo: ')
            email = input('Digite o email: ')
            telefone = int(input('Digite o telefone: '))
            curso = input('Digite o curso: ')
            voucher = randint(100, 400)
            cadastro['nome'].append(nome)
            cadastro['email'].append(email)
            cadastro['telefone'].append(telefone)
            cadastro['curso'].append(curso)
            cadastro['voucher'].append(voucher)
            print('Numero do voucher:', voucher)
        print('Cadastro realizado com sucesso!!')

    elif opcao == 2:
        print('***Opção', opcao, ': Visualizar Cadastro***')

        if len(cadastro['nome']) >= 1:
            for i, j in cadastro.items():
                print('-' * 20)
                print('{} = {}'.format(i,j))

        else:
            print('Não há cadastro')

    elif opcao == 3:
        encerrar = True
        print('Programa encerrado!!')
