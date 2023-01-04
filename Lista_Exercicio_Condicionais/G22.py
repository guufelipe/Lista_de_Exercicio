#É COPAAAAA!!!!! Estamos em clima de festa com o possível hexa do nosso Brasil e por isso nada mais justo do que
# uma questão de programação com esse tema. Mas não se preocupe se você não entender nada de futebol, você pode não
# ser o especialista nesse esporte, mas a gente sabe que é expert em programar.
#A primeira fase dos jogos da copa é a fase de grupos em que 4 times jogam entre si e as duas seleções com melhores
# pontuações se classificam para próxima fase. Como o programa que contabiliza esses pontos da FIFA pifou, nada mais
# justo do que você, aluno do CIn, fazer um programa que receba os times e o resultado dos jogos de cada um e retorne
# quais as duas seleções do grupo passam para próxima fase.
#Como geralmente em cada grupo sempre tem um time mais fraco, considere que um dos quatro times perdeu todos os jogos
# e já não tem mais chances de avançar na competição.
#O sistema de pontuação da Copa do Mundo é o tradicional aplicado em competições de futebol: a vitória dá 3 pontos, o
# empate, 1 ponto; a derrota, nenhum ponto.
#obs.: Não terá empate nos pontos das duas seleções que mais pontuarem

#TIME 1
pontos_time_1 = 0
nome_time_1 = input()
resultado_jogo_1_time_1 = input()
resultado_jogo_2_time_1 = input()
#Pontos time 1
if resultado_jogo_1_time_1 == "Ganhou":
    pontos_time_1 += 3
elif resultado_jogo_1_time_1 == "Empatou":
    pontos_time_1 += 1

if resultado_jogo_2_time_1 == "Ganhou":
    pontos_time_1 += 3
elif resultado_jogo_2_time_1 == "Empatou":
    pontos_time_1 += 1

#TIME 2
pontos_time_2 = 0
nome_time_2 = input()
resultado_jogo_1_time_2 = input()
resultado_jogo_2_time_2 = input()
#Pontos time 2
if resultado_jogo_1_time_2 == "Ganhou":
    pontos_time_2 += 3
elif resultado_jogo_1_time_2 == "Empatou":
    pontos_time_2 += 1

if resultado_jogo_2_time_2 == "Ganhou":
    pontos_time_2 += 3
elif resultado_jogo_2_time_2 == "Empatou":
    pontos_time_2 += 1

#TIME 3
pontos_time_3 = 0
nome_time_3 = input()
resultado_jogo_1_time_3 = input()
resultado_jogo_2_time_3 = input()
#Pontos time 2
if resultado_jogo_1_time_3 == "Ganhou":
    pontos_time_3 += 3
elif resultado_jogo_1_time_3 == "Empatou":
    pontos_time_3 += 1

if resultado_jogo_2_time_3 == "Ganhou":
    pontos_time_3 += 3
elif resultado_jogo_2_time_3 == "Empatou":
    pontos_time_3 += 1

#classificados / eliminados

if pontos_time_1 < pontos_time_2 and pontos_time_1 < pontos_time_3:
    print(f'Parabéns aos países {nome_time_2} e {nome_time_3}, vocês estão classificados para as oitavas de finais!!!')

if pontos_time_2 < pontos_time_1 and pontos_time_2 < pontos_time_3:
    print(f'Parabéns aos países {nome_time_1} e {nome_time_3}, vocês estão classificados para as oitavas de finais!!!')

if pontos_time_3 < pontos_time_1 and pontos_time_3 < pontos_time_2:
    print(f'Parabéns aos países {nome_time_1} e {nome_time_2}, vocês estão classificados para as oitavas de finais!!!')