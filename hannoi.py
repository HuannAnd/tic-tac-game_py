pines_hannoi_num = 10
A = "A"
B = "B"
C = "C"

def Hannoi(pines, start_pine, aux_pine, destiny_pine):
  if pines > 0:
    first_hannoi = Hannoi(pines - 1, start_pine, destiny_pine, aux_pine)

    second_hannoi = Hannoi(pines - 1, aux_pine, start_pine, destiny_pine)

    return second_hannoi + 1 + first_hannoi
  return 0

print("Insira a quantidade de pinos da torre de Hannoi")
num_of_pines = int(input())

final_hannoi_plays = Hannoi(num_of_pines, A, B, C)
print(f"Numero de jogadas {final_hannoi_plays}")
