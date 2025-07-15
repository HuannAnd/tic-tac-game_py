test_vector = [10, 19, 7, 5, 19, 7, 8, 10, 7, 12]


def get_mode_first(vector):
    list_of_elements_not_repeated = []
    index_of_most_repeated_element = 0
    counter_of_most_repeated_element = 0

    for element in vector:
        if not (element in list_of_elements_not_repeated):
            list_of_elements_not_repeated.append(element)

    for occurrence in list_of_elements_not_repeated:
        counter = 0

        for j in range(len(vector)):
            if vector[j] == occurrence:
                counter += 1

                if counter > counter_of_most_repeated_element:
                    counter_of_most_repeated_element = counter
                    index_of_most_repeated_element = j

    return [counter_of_most_repeated_element, vector[index_of_most_repeated_element]]


def get_mode_second(vector):
    list_of_elements = [0] * len(vector)
    counter_of_most_repeated_element = 0
    index_of_most_repeated_element = 0

    for i in range(len(vector)):
        current_element_tell = vector[i]
        counter = 1

        for j in range(i + 1, len(vector)):
            if j == current_element_tell:
                counter += 1

                if counter > counter_of_most_repeated_element:
                    counter_of_most_repeated_element = counter
                    index_of_most_repeated_element = j

    return [counter_of_most_repeated_element, vector[index_of_most_repeated_element]]


def get_mode_3(vector):
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



print(get_mode_first(test_vector))
print(get_mode_second(test_vector))
