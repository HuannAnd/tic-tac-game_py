import os
import time

def clear_terminal():
  os.system("clss||clear")

three_seconds = 3
print("Bem-vindo ao Jogo da Velha")
time.sleep(three_seconds)
clear_terminal()

table = []
round = 0
choices = []

print("Digite o nome do primeiro player:")
first_player_name = input()
print("Digite o nome do segundo player:")
second_player_name = input()

def draw_tic_tac_toe(table):
  print(f"{table[0]}\n{table[1]}\n{table[2]}")

print("O jogo começou!")
draw_tic_tac_toe()

# escolhendo o jogador da vez
round_player = first_player_name if round % 2 == 0 else second_player_name
round_symbol = "X" if round % 2 == 0 else "O"

print(f"{round_player}: Digite uma das seguintes casas de 1 a 9")
choice = int(input()) - 1 # Convertendo o input de 1 a 9 para 0 a 8 (ordem do array em python)

column = play // 3
row = play % 3 

play = table[row][column]

table[row][column] = round_symbol
choices = []




