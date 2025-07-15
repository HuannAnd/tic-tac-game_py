test_vector = [7, 19, 4, 10, 8, 1, 18, 6, 3, 12]


def bubble_sort(vector):
    for i in range(len(vector) - 1):
        if vector[i] > vector[i + 1]:
          temporary_value = vector[i]
          vector[i] = vector[i + 1]
          vector[i + 1] = temporary_value

          
