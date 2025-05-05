test_vector = [1, 2, 3, 4, 5, 6, 8]

def binary_search(vector, el, start = 0, end = None):
  if end is None:
    end = len(vector)

  if start >= end:
    middle =  (start + end) // 2

    if vector[middle] == el:
      return middle
    
    elif vector[middle] > el:
      new_end = middle - 1
      return binary_search(vector, el, start, new_end)

    elif vector[middle] < el:
      new_start = middle + 1
      return binary_search(vector, el, new_start, end)
  return -1

def custom_message(val):
  return f"Foi encontrado no vetor" if val != 1 else "Não foi encontrado"
  

print("Digite o número procurado no vetor: ", test_vector)
current_number_searched = int(input())
binary_search_result = binary_search(test_vector, current_number_searched)

print(f"O número {current_number_searched}, {custom_message(binary_search())}")