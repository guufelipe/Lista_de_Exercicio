time_1 = input()
ataque_1 = int(input())
def_1 = int(input())
folego_1 = int(input())
gols_1 = 0
canseira_1 = 1 - (5 - folego_1)/10

time_2 = input()
ataque_2 = int(input())
def_2 = int(input())
folego_2 = int(input())
gols_2 = 0
canseira_2 = 1 - (5 - folego_2)/10

sorte_1 = int(input())
sorte_2 = int(input())
sorte_3 = int(input())
sorte_4 = int(input())

# Primeiero tempo. Time 1 ataca
ataque = ataque_1 # Ataque e defesa sao variaveis temporárias
defesa = def_2
if sorte_1 == 1:
    ataque += 2
else:
    defesa += 2
  
if ataque >= defesa:
    mensagem_1 = f'GOOOOOOOOOOOOLLLLLL DO TIME {time_1}!!!'
    gols_1 += 1
else:
    mensagem_1 = f'O ataque é interrompido! Ótima defesa do time {time_2}'

# Primeiro tempo. Time 2 ataca
ataque = ataque_2 * canseira_2
defesa = def_1 * canseira_1
if sorte_2 == 1:
    ataque += 2
else:
    defesa += 2
    
if ataque >= defesa:
    mensagem_2 = f'GOOOOOOOOOOOOLLLLLL DO TIME {time_2}!!!'
    gols_2 += 1    
else:
    mensagem_2 = f'O ataque é interrompido! Ótima defesa do time {time_1}'
    
print(f"""Início de jogo!
1° tempo:
{time_1} [0-0] {time_2}
O time {time_1} vem pressionando.
{mensagem_1}
O time {time_2} vem pressionando.
{mensagem_2}
2° tempo:
{time_1} [{gols_1}-{gols_2}] {time_2}""")

# Segundo tempo. Time 2 ataca
ataque = ataque_2 * (canseira_2 ** 2)
defesa = def_1 * (canseira_1 ** 2)
if sorte_3 == 1:
    ataque += 2
else:
    defesa += 2
    
if ataque >= defesa:
    mensagem_3 = f'GOOOOOOOOOOOOLLLLLL DO TIME {time_2}!!!'
    gols_2 += 1
else:
    mensagem_3 = f'O ataque é interrompido! Ótima defesa do time {time_1}'

# Segundo tempo. Time 1 ataca
ataque = time_1 = input()
ataque_1 = int(input())
def_1 = int(input())
folego_1 = int(input())
gols_1 = 0
canseira_1 = 1 - (5 - folego_1)/10

time_2 = input()
ataque_2 = int(input())
def_2 = int(input())
folego_2 = int(input())
gols_2 = 0
canseira_2 = 1 - (5 - folego_2)/10

sorte_1 = int(input())
sorte_2 = int(input())
sorte_3 = int(input())
sorte_4 = int(input())

# Primeiero tempo. Time 1 ataca
ataque = ataque_1 # Ataque e defesa sao variaveis temporárias
defesa = def_2
if sorte_1 == 1:
    ataque += 2
else:
    defesa += 2
  
if ataque >= defesa:
    mensagem_1 = f'GOOOOOOOOOOOOLLLLLL DO TIME {time_1}!!!'
    gols_1 += 1
else:
    mensagem_1 = f'O ataque é interrompido! Ótima defesa do time {time_2}'

# Primeiro tempo. Time 2 ataca
ataque = ataque_2 * canseira_2
defesa = def_1 * canseira_1
if sorte_2 == 1:
    ataque += 2
else:
    defesa += 2
    
if ataque >= defesa:
    mensagem_2 = f'GOOOOOOOOOOOOLLLLLL DO TIME {time_2}!!!'
    gols_2 += 1    
else:
    mensagem_2 = f'O ataque é interrompido! Ótima defesa do time {time_1}'
    
print(f"""Início de jogo!
1° tempo:
{time_1} [0-0] {time_2}
O time {time_1} vem pressionando.
{mensagem_1}
O time {time_2} vem pressionando.
{mensagem_2}
2° tempo:
{time_1} [{gols_1}-{gols_2}] {time_2}""")

# Segundo tempo. Time 2 ataca
ataque = ataque_2 * (canseira_2 ** 2)
defesa = def_1 * (canseira_1 ** 2)
if sorte_3 == 1:
    ataque += 2
else:
    defesa += 2
    
if ataque >= defesa:
    mensagem_3 = f'GOOOOOOOOOOOOLLLLLL DO TIME {time_2}!!!'
    gols_2 += 1
else:
    mensagem_3 = f'O ataque é interrompido! Ótima defesa do time {time_1}'

# Segundo tempo. Time 1 ataca
ataque = time_1 = input()
ataque_1 = int(input())
def_1 = int(input())
folego_1 = int(input())
gols_1 = 0
canseira_1 = 1 - (5 - folego_1)/10

time_2 = input()
ataque_2 = int(input())
def_2 = int(input())
folego_2 = int(input())
gols_2 = 0
canseira_2 = 1 - (5 - folego_2)/10

sorte_1 = int(input())
sorte_2 = int(input())
sorte_3 = int(input())
sorte_4 = int(input())

# Primeiero tempo. Time 1 ataca
ataque = ataque_1 # Ataque e defesa sao variaveis temporárias
defesa = def_2
if sorte_1 == 1:
    ataque += 2
else:
    defesa += 2
  
if ataque >= defesa:
    mensagem_1 = f'GOOOOOOOOOOOOLLLLLL DO TIME {time_1}!!!'
    gols_1 += 1
else:
    mensagem_1 = f'O ataque é interrompido! Ótima defesa do time {time_2}'

# Primeiro tempo. Time 2 ataca
ataque = ataque_2 * canseira_2
defesa = def_1 * canseira_1
if sorte_2 == 1:
    ataque += 2
else:
    defesa += 2
    
if ataque >= defesa:
    mensagem_2 = f'GOOOOOOOOOOOOLLLLLL DO TIME {time_2}!!!'
    gols_2 += 1    
else:
    mensagem_2 = f'O ataque é interrompido! Ótima defesa do time {time_1}'
    
print(f"""Início de jogo!
1° tempo:
{time_1} [0-0] {time_2}
O time {time_1} vem pressionando.
{mensagem_1}
O time {time_2} vem pressionando.
{mensagem_2}
2° tempo:
{time_1} [{gols_1}-{gols_2}] {time_2}""")

# Segundo tempo. Time 2 ataca
ataque = ataque_2 * (canseira_2 ** 2)
defesa = def_1 * (canseira_1 ** 2)
if sorte_3 == 1:
    ataque += 2
else:
    defesa += 2
    
if ataque >= defesa:
    mensagem_3 = f'GOOOOOOOOOOOOLLLLLL DO TIME {time_2}!!!'
    gols_2 += 1
else:
    mensagem_3 = f'O ataque é interrompido! Ótima defesa do time {time_1}'

# Segundo tempo. Time 1 ataca
ataque = ataque_1 * (canseira_1 ** 3)
defesa = def_2 * (canseira_2 ** 3)
if sorte_4 == 1:
    ataque += 2
else:
    defesa += 2
    
if ataque >= defesa:
    mensagem_4 = f'GOOOOOOOOOOOOLLLLLL DO TIME {time_1}!!!'
    gols_1 += 1
else:
    mensagem_4 = f'O ataque é interrompido! Ótima defesa do time {time_2}'
    
# Fim de jogo
if gols_1 == gols_2:
    mensagem_resultado = 'Temos um empate! Será decidido em breve nos pênaltis. Fique ligado!'
elif gols_1 > gols_2:
    mensagem_resultado = f'ACABOOOOU!! O TIME {time_1} É O CAMPEÃO!!!'
else:
    mensagem_resultado = f'Fim de jogo! O time {time_2} é campeão.'
    
print(f"""O time {time_2} vem pressionando.
{mensagem_3}
O time {time_1} vem pressionando.
{mensagem_4}
{time_1} [{gols_1}-{gols_2}] {time_2}
{mensagem_resultado}""") * (canseira_1 ** 3)
defesa = def_2 * (canseira_2 ** 3)
if sorte_4 == 1:
    ataque += 2
else:
    defesa += 2
    
if ataque >= defesa:
    mensagem_4 = f'GOOOOOOOOOOOOLLLLLL DO TIME {time_1}!!!'
    gols_1 += 1
else:
    mensagem_4 = f'O ataque é interrompido! Ótima defesa do time {time_2}'
    
# Fim de jogo
if gols_1 == gols_2:
    mensagem_resultado = 'Temos um empate! Será decidido em breve nos pênaltis. Fique ligado!'
elif gols_1 > gols_2:
    mensagem_resultado = f'ACABOOOOU!! O TIME {time_1} É O CAMPEÃO!!!'
else:
    mensagem_resultado = f'Fim de jogo! O time {time_2} é campeão.'
    
print(f"""O time {time_2} vem pressionando.
{mensagem_3}
O time {time_1} vem pressionando.
{mensagem_4}
{time_1} [{gols_1}-{gols_2}] {time_2}
{mensagem_resultado}""") * (canseira_1 ** 3)
defesa = def_2 * (canseira_2 ** 3)
if sorte_4 == 1:
    ataque += 2
else:
    defesa += 2
    
if ataque >= defesa:
    mensagem_4 = f'GOOOOOOOOOOOOLLLLLL DO TIME {time_1}!!!'
    gols_1 += 1
else:
    mensagem_4 = f'O ataque é interrompido! Ótima defesa do time {time_2}'
    
# Fim de jogo
if gols_1 == gols_2:
    mensagem_resultado = 'Temos um empate! Será decidido em breve nos pênaltis. Fique ligado!'
elif gols_1 > gols_2:
    mensagem_resultado = f'ACABOOOOU!! O TIME {time_1} É O CAMPEÃO!!!'
else:
    mensagem_resultado = f'Fim de jogo! O time {time_2} é campeão.'
    
print(f"""O time {time_2} vem pressionando.
{mensagem_3}
O time {time_1} vem pressionando.
{mensagem_4}
{time_1} [{gols_1}-{gols_2}] {time_2}
{mensagem_resultado}""")