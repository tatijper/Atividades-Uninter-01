# Atividades-Uninter-01
Projetos desenvolvidos para trabalho de Lógica de programação e Algoritimos

Exercício 1:
A ampliação do Ensino Fundamental para nove anos de duração, tornou a matrícula da criança obrigatória a partir dos seis anos de idade. Implemente um programa que fornecidos o nome e a idade de um criança classifique-a em uma das seguintes etapas de ensino:
Ensino                  Faixa etária
Educaçao Infantil       1 a 5 anos
Ensino Fundamental I    6 a 10 anos
Ensino Fundamental II   11 a 14
Ensino médio           maiores de 15 anos
O usuário deve ainda ter a opção de escolher se quer encerrar o programa ou não.

Exercício 2:
Faça um programa que solicite que o usuário digite um nome. O programa deve imprimir na tela o nome convertido no seguinte formato:
L*C!@N&
Para isso, o programa deve ser capaz de converter o nome digitado para maiúsculas e substituir as vogais pelos símbolos apresentados na tabela abaixo.

A - @

E - &

I - !

O - #

U - *

Exercício 3:
Implementar um jogo que é popular entre as crianças: um hotel onde os hóspedes têm algumas restrições quanto a localização de seu quarto, seguindo as seguintes regras:
• O rato não pode ficar ao lado do gato.
• O cão não pode ficar ao lado do osso.
• O gato não pode ficar ao lado do cão.
• O queijo não pode ficar ao lado do rato
O jogo é composto por 4 fases, onde cada fase (a partir da fase 2) só é desbloqueada se a anterior for concluída com êxito.
Em todas as fases, as células em cinza representam os quartos indisponíveis, portanto não podem ser alocados. As letras nas células correspondem aos seguintes hóspedes:

G – GATO

C – CÃO

R – RATO

O – OSSO

Q – QUEIJO.

Ao término de cada fase o jogador deverá receber uma mensagem informando se teve êxito ou não na sua resposta. Se não teve êxito, o programa se encerra mostrando a mensagem: “Você perdeu!”. Se teve exito a próxima fase é desbloqueada, ao terminar a ultima fase com exito uma mensagem de “VocÊ ganhou!” é mostrada na tela.
Na Fase 1, o jogador deve alocar o RATO e o GATO.

Na segunda fase o jogador deve alocar : CÃO, CÃO E OSSO.

Na fase 3 o jogador deverá alocar : GATO, RATO E OSSO,

Na fase 4, o jogador deverá alocar: QUEIJO, QUEIJO, OSSO.

Exercício 4:
Uma escola de cursos de TI oferece vouchers para que os participantes possam assistir algumas aulas gratuitas de Python. Para isso o participante que deseja assistir as aulas gratuitas desse curso específico, deve fazer uma inscrição para receber o voucher. Implemente um programa que armazene as inscrições para o curso. O programa deverá armazenar para cada inscrição:
Um código único para o voucher
Nome
Email
Telefone
Curso
O programa deverá apresentar um menu de opções ao usuário:
1 –inscrição: ao selecionar essa opção, o usuário deverá ser capaz de informar todos os dados da inscrição. O código do voucher deve ser preenchido automaticamente pelo sistema, e o usuário não deve ter a opção de alterar esse código;
2 – visualizar inscrição: ao selecionar essa opção, o programa deverá imprimir, na tela, para cada reserva, todos os dados dessa inscrição. Caso nenhuma inscrição tenha sido cadastrada ao selecionar essa opção, o programa deverá exibir a mensagem “nenhuma inscrição cadastrada”.;
0 – Encerrar: ao selecionar essa opção, o programa se encerra.
Caso o usuário escolha uma opção que não conste no menu, o programa deverá exibir uma mensagem de erro, por exemplo, “Erro: digite uma opção válida!”.

