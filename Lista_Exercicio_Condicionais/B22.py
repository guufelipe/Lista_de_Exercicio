#Pedro Baptista, seu monitor de IP, está afundado em dívidas e decidiu pedir um empréstimo ao banco para apostar 
# todo o seu dinheiro nas maiores zebras dos jogos da Copa do Mundo do Catar para ganhar a maior quantidade de 
# dinheiro possível, mas ele não sabe como contabilizar o dinheiro que ganhou ou perdeu nas apostas.
#Seu trabalho é informar o resultado do jogo que Pedro apostou e os ganhos que ele teve, além de impedir
# que ele aposte em resultados que não são zebra.



selecao1 = (input())
selecao2 = (input())
aposta = (int(input()))
probabilidade = float((input()))
resultado = (input())

if probabilidade < 0.5 :
  valor = int(aposta * (1 + (0.5 - probabilidade)**2 *100))

  if resultado == "Ganhou":
    if probabilidade < 0.5 and probabilidade > 0.4:
      print(f"Não foi um palpite tão arriscado, todos sabiam que {selecao1} não estava muito atrás de {selecao2}")
      print(f"Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta")
    elif probabilidade <= 0.4 and probabilidade > 0.3:
      print(f"Eu pensava que {selecao2} iria ganhar, mas nunca duvidei que a {selecao1} pudesse ganhar essa partida")
      print(f"Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta")
    elif probabilidade <= 0.3 and probabilidade > 0.2:
      print(f"Uau! que jogo foi esse?? {selecao1} surpreendeu a todos nós…")
      print(f"Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta")
    elif probabilidade <= 0.2 and probabilidade > 0.1:
      print(f"Essa é a copa das zebras?? O impossível aconteceu hoje nessa partida, como que {selecao1} ganhou de {selecao2}, alguém me explica?")
      print(f"Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta")
    elif probabilidade <= 0.1 :
      print(f"PEDROOOOO, você tá rico!! ninguém, absolutamente ninguém apostou na {selecao1}, somente você!")
      print(f"Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta")
  else: 
    print(f"Pedro, infelizmente você está no fundo do poço, se endividou completamente e não temos o que fazer…")
    print(f"Você poderia ter ganhado R${valor}, mas perdeu R${aposta}")
    
else : 
  print("Pedro, você está proibido de apostar nos favoritos, só em zebra, lembra?")