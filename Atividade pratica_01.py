continuar='1'

#laço de repetição inicial para gerar o loop do programa até o usuario solicitar o fim da utilização
while(continuar == '1'):
#inserção de variáveis
    nome=input('Digite o nome: ')
    idade=int(input('Digite a idade: '))
#condições para inserir a criança dentro das tabelas escolares pré estabelecidas
    if 1 <= idade <= 5:
        print('Educação Infantil')
    elif 6<= idade <=10:
        print('Ensino Fundamental I')
    elif 11<= idade <=14:
        print('Ensino Fundamental II')
    elif 15<= idade <=18:
        print('Ensino Médio')
#condição limitadora de idade máxima para o período escolar
    elif idade>=19:
        print('Inválido')
    continuar=input('Deseja continuar? 1-Sim | 2-Não : ')
    if continuar!= '1':
        print('Programa encerrado!')




