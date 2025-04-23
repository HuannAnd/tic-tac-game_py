import os
import time


def clear_terminal():
    os.system("cls")


three_seconds = 0
print("Bem-vindo ao Jogo da Velha")
time.sleep(three_seconds)
clear_terminal()

table = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]
winner_plays = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],  # Vitorias em linhas
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],  # Vitorias em colunas
    [0, 4, 8],
    [2, 5, 6],  # Vitorias nas diagonais
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
    if round == 9:
        return True


def is_game_tied():
    return round == 9


def has_winner():
    round_player_choices = first_player_plays if round % 2 == 0 else second_player_plays
    print(f"Player choices {round_player_choices}")

    for win_play in winner_plays:
        (a, b, c) = win_play
        print(f"Current game in analysis {win_play}")

        if (
            a in round_player_choices
            and b in round_player_choices
            and c in round_player_choices
        ):
            return True

    return False


def is_play_made(choice):
    return choice in choices


def is_choice_between_one_and_nine(choice):
    return choice >= 0 and choice <= 8


def get_user_response():
    while True:
        choice = int(input()) - 1
        print(f"casa escolhida {choice}")
        print(f"if {is_choice_between_one_and_nine(choice)}")

        if not is_choice_between_one_and_nine(choice):
            print(f"Digite uma casa entre 1 a 9")
            continue
        if is_play_made(choice):
            print(
                f"A casa {choice + 1} já está preenchida, por favor faça outra jogada"
            )
            continue

        return choice


print("O jogo começou!")
while True:
    # clear_terminal()
    draw_tic_tac_toe(table)

    # escolhendo o jogador da vez
    round_player = first_player_name if round % 2 == 0 else second_player_name
    round_symbol = "X" if round % 2 == 0 else "O"
    round_player_plays = first_player_plays if round % 2 == 0 else second_player_plays

    print(f"{round_player} ({round_symbol}): Digite uma das seguintes casas de 1 a 9")
    # choice = int(input()) - 1 # Convertendo o input de 1 a 9 para 0 a 8 (ordem do array em python)
    choice = get_user_response()

    row = choice // 3
    column = choice % 3

    # play = table[row][column]

    table[row][column] = round_symbol
    choices.append(choice)
    round_player_plays.append(choice)


    if round >= 4:
        print("Caiu no round >= 4")

        if has_winner():
            print(f"O jogo terminou\n{round_player} Venceu!")
            break

    if is_game_tied():
        print("O jogo acabou, deu empate!")
        break

    round += 1
