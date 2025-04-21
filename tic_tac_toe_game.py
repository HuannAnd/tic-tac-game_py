import os
import time

def clear_terminal():
  os.system("cls")

three_seconds = 3
print("Bem-vindo ao Jogo da Velha")
time.sleep(three_seconds)
clear_terminal()

table = [
  ["1", "2", "3"],
  ["4", "5", "6"],
  ["7", "8", "9"],
]
winner_plays = [
  [1,2,3], [4,5,6], [7, 8, 9], # Vitorias em linhas
  [1,4,7], [2,5,8], [3, 6, 9], # Vitorias em colunas
  [1,5, 9], [3, 6, 7] # Vitorias nas diagonais
]
round = 0
choices = []
is_finished = False

print("Digite o nome do primeiro player:")
first_player_name = input()
first_player_plays = []
print("Digite o nome do segundo player:")
second_player_name = input()
second_player_plays = []

def draw_tic_tac_toe(table):
  print(f"{table[0]}\n{table[1]}\n{table[2]}")

def game_is_finished():
  if(round == 9):
    return True


def is_game_tied():
  if round == 9 and 

def has_winner():
  round_player_choices = first_player_plays if round % 2 == 0 else second_player_plays

  for win_play in winner_plays:
    (a, b, c) = win_play

    if(
      a in round_player_choices and 
      b in round_player_choices and 
      c in round_player_choices
      ):
      return True
  
  return False

print("O jogo começou!")
while is_finished:
  draw_tic_tac_toe(table)

  # escolhendo o jogador da vez
  round_player = first_player_name if round % 2 == 0 else second_player_name
  round_symbol = "X" if round % 2 == 0 else "O"

  print(f"{round_player}: Digite uma das seguintes casas de 1 a 9")
  choice = int(input()) - 1 # Convertendo o input de 1 a 9 para 0 a 8 (ordem do array em python)

  column = choice // 3
  row = choice % 3 

  # play = table[row][column]

  table[row][column] = round_symbol
  choices.append(choice)
  round+=1


