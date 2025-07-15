def search_less_and_greater_element(vector, concat_vector):
  new_vector = []

  largest_num = get_largest_num(vector)
  smallest_num = get_smallest_number(vector)

  if largest_num != smallest_num:
    x = search_less_and_greater_element() 
    k
  
  return concat_vector

def get_smallest_number(vector):
  smallest_num = vector[i]

  for i in range(1, len(vector ) - 1):
    if smallest_num > vector[i]:
      smallest_num = vector[i]
    
  return smallest_num

def get_largest_num(vector):
  largerst_num = vector[i]

  for i in range(1, len(vector ) - 1):
    if largerst_num > vector[i]:
      largerst_num = vector[i]
    
  return largerst_num