matrix_filename = input()

def is_square_matrix(quantity):
  for num in range(1, quantity + 1):
    if num ** 2 == quantity:
      return True
  
  return False

def convert_matrix_in_vector(matrix):
  vector = []

  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      vector.append(matrix[row][col])
  
  return vector

def is_simetric_matrix(matrix, transpose):
  t_cols = len(transpose) 
  cols = len(matrix)
  t_rows = len(transpose[0])
  rows = len(transpose[0])

  if rows == cols and  t_rows == rows and t_cols == cols:
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        if matrix[i][j] != transpose[i][j]:
          return False

    return True
  return False
   
def transpose_matrix(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  transpose = [[0 for _ in range(rows)] for _ in range(cols)]

  for i in range(rows):
    for j in range(cols):
      transpose[i][j] = matrix[j][i]
  
  return transpose


def add_all_elements(concatenated, concataner):
  for el in concataner:
    concatenated.append(el)
  
  return None

def get_mode(vector):
    aux_vector = [0] * len(vector)

    for i in range(len(aux_vector)):
        aux_vector[i] = 1

        for j in range(i + 1, len(aux_vector)):
            if vector[j] == vector[i]:
              aux_vector[i] += 1
    
    where_mode = 0
    for i in range(1, len(aux_vector)):
      if aux_vector[i] > aux_vector[where_mode]:
          where_mode = i
    
    return [vector[where_mode], aux_vector[where_mode]]

with open(matrix_filename, mode="r", encoding="utf-8") as current:
  number_of_elements = 0
  document = current.readlines()
  matrix = []
  cols = len(list(document))

  for line in document:
    all_values = list(map(int, line.split()))
    rows = len(all_values)

    matrix.append(all_values)

  print("Numero de colunas ", cols)
  print("Numero de linhas ", rows)
  is_squared_matrix = rows == cols

  if is_squared_matrix:
    transpose_of_matrix = transpose_matrix(matrix)

    if is_simetric_matrix(matrix, transpose_of_matrix):
      print("A matriz é quadrada e simétrica")
    else:
      print("A matriz é quadrada")
  
  else:
    print("A matriz não é quadrada")
  

  matrix_as_vector = convert_matrix_in_vector(matrix)
  [mode_of_matrix, _] = get_mode(matrix_as_vector)

  print("A moda da matriz é %d" % mode_of_matrix)