import heapq

lista = [1, 2, 3,3,3,3, 1,1,1]
lista_saida = []

novo_heap = heapq.heapify(lista)
heapq.heapify(lista)

for i in range(len(lista)):
  lista_saida.append(heapq.heappop(lista))

print(lista_saida)