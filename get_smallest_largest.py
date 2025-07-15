test_vector = [4, 18, 4, 10, 18, 5, 19, 1, 3, 18]

def get_smallest_largets(vector):
  largest = vector[0]
  smallest = vector[0]
  vector_length = len(vector)

  for i in range(1, vector_length):
    if smallest > vector[i]:
      smallest = vector[i]
    elif largest < vector[i]:
      largest = vector[i]
  
  return [smallest, largest]

print(get_smallest_largets(test_vector)) # exptected [1, 18]