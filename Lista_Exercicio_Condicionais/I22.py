#Depois de conseguir avançar na fase de grupos, a seleção de Tite chega como uma forte candidata a vencer o torneio,
# mas Tite não quis esperar o final da copa para saber se o brasil ia ser campeão ou não, então ele decidiu pedir para
# você fazer uma simulação com o mata-mata da seleção brasileira para ver o que ia acontecer.
#Ele pediu para fazer de um jeito que o fator Favoritismo, sendo ele um numero inteiro, fosse ser algo muito presente na
# sua simulação.
#Você vai receber os resultados que o brasil vai ter das fases do mata-mata, das oitavas até a semifinal (considerando que
# o Brasil vai chegar até lá). Nos resultados, o Brasil pode tanto avançar quanto ser eliminado em qualquer fase.
#Caso o brasil perca antes de chegar a final, ele será eliminado, e você não receberá as entradas das fases seguintes
# consequentemente.
#Caso ocorra um empate, aí é que o favoritismo começa a entrar em cena, porque ele é o fator de desempate nesse caso, ou
# seja, em caso de empate, passa a seleção com o maior favoritismo (caso elas empatem no favoritismo também, passa o
# Brasil porque Tite é clubista!).
#Caso o Brasil vença a partida (sem contar a final) o seu favoritismo aumenta dependendo do placar do jogo. Se o brasil
# vencer por 1 gol de diferença, seu favoritismo aumenta em 10 pontos, se vencer por 2 gols de diferença, aumenta em 20
# pontos o favoritismo, e caso vença por 3 ou mais gols, aumenta em 30 pontos o favoritismo brasileiro.
#A final já vai ser diferente, nela você não vai receber um resultado caso o brasil chegue nela, você só saberá o oponente
# do Brasil e o Favoritismo que ele chega, e só com o favoritismo, definir quem vai ser o campeão (caso haja empate no
# favoritismo, ganha quem tem mais copas do mundo ;) Ps. é o Brasil sempre)
#OBS: Das oitavas até a final são 4 partidas, mas lembre-se que a última (final), possui uma entrada diferente, e que não
# necessariamente o Brasil jogará as 4 partidas.
#OBS: As funções exit() e quit() não podem ser utilizadas nessa questão.


dfr_gols = 0
fim_jogo = False

##Jogo 1(OITAVAS DE FINAL)
favoritismoBr = int(input())
nomeOponente1 = input()
favoritismoOponente1 = int(input())
golsBR1 = int(input())
golsOPO1 = int(input())
dfr_gols = golsBR1 - golsOPO1

if golsBR1 < golsOPO1:
    if golsBR1 < golsOPO1:
        fim_jogo = True
    print(f'Infelizmente essa seleção dx {nomeOponente1} era muito forte para o Brasil.')
    
if not fim_jogo and (golsBR1 > golsOPO1):
    if dfr_gols == 1:
        favoritismoBr += 10
    elif dfr_gols == 2:
        favoritismoBr += 20
    elif dfr_gols >= 3:
        favoritismoBr += 30
    print("Quem é que segura o Brasil???")

if not fim_jogo and (golsBR1 == golsOPO1):
    if (favoritismoBr < favoritismoOponente1):
            fim_jogo = True
            print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
    else:
        print("No sufoco, o Brasil conseguiu ganhar!!!")
        
##Jogo 2(QUARTAS DE FINAL)
if not fim_jogo:
    nomeOponente2 = input()
    favoritismoOponente2 = int(input())
    golsBR2 = int(input())
    golsOPO2 = int(input()) 
    dfr_gols = golsBR2 - golsOPO2

    if not fim_jogo and (golsBR2 < golsOPO2):
        if golsBR2 < golsOPO2:
            fim_jogo = True
        print(f'Infelizmente essa seleção dx {nomeOponente2} era muito forte para o Brasil.')
        
    if not fim_jogo and (golsBR2 > golsOPO2):
        if dfr_gols == 1:
            favoritismoBr += 10
        elif dfr_gols == 2:
            favoritismoBr += 20
        elif dfr_gols >= 3:
            favoritismoBr += 30
        print("Quem é que segura o Brasil???")
        
    if not fim_jogo and (golsBR2 == golsOPO2):
        if (favoritismoBr < favoritismoOponente2):
                fim_jogo = True
                print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
        else:
            print("No sufoco, o Brasil conseguiu ganhar!!!")

##Jogo 3(SEMI-FINAL)

if not fim_jogo:
    nomeOponente3 = input()
    favoritismoOponente3 = int(input())
    golsBR3 = int(input())
    golsOPO3 = int(input())
    dfr_gols = golsBR3 - golsOPO3

    if not fim_jogo and (golsBR3 < golsOPO3):
        if golsBR3 < golsOPO3:
            fim_jogo = True
        print(f'Infelizmente essa seleção dx {nomeOponente3} era muito forte para o Brasil.')
        
    if not fim_jogo and (golsBR3 > golsOPO3):
        if dfr_gols == 1:
            favoritismoBr += 10
        elif dfr_gols == 2:
            favoritismoBr += 20
        elif dfr_gols >= 3:
            favoritismoBr += 30
        print("Quem é que segura o Brasil???")
        
    if not fim_jogo and (golsBR3 == golsOPO3):
        if (favoritismoBr < favoritismoOponente3):
                fim_jogo = True
                print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
        else:
            print("No sufoco, o Brasil conseguiu ganhar!!!")

##Jogo 4( FINAL) 
if not fim_jogo:
    nomeOponente4 = input() 
    favoritismoOponente4 = int(input())
    if favoritismoBr > favoritismoOponente4:
        print("O BRASIL VAI SER HEXAAAAAAAA")
    elif favoritismoBr == favoritismoOponente4:
        print("O BRASIL VAI SER HEXAAAAAAAA")
    else:
        print(f'O nosso Brasil foi vice, não conseguindo bater a seleção dx {nomeOponente4} na simulação')