numero_de_instancias = int(input())
counter_one = 0 
while counter_one < numero_de_instancias:
  pares_de_linhas,linhas_da_letra = map(int,input.split())
  linhas_totais = 2*pares_de_linhas
  counter_two = 0
  japones_portugues = dict()
  while counter_two < linhas_totais:
    palavra_em_japones = input()
    palavra_em_portugues = input()
    japones_portugues[palavra_em_japones] = palavra_em_portugues
    counter_two+=1
  counter_three = 0
  while counter_three < linhas_da_letra:

