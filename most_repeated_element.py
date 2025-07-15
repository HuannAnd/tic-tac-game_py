test_vector = [1, 1, 2, 2, 3]
    
def most_repeated_element(vector):
    concurr_vector = []
    range_vector = len(vector)
    index_of_most_repeated_element = 0
    counter_of_most_repeated_element = 0

    for k in range(range_vector):
        if not (k in concurr_vector):
            concurr_vector.append(k)

    for j in range(len(concurr_vector)):
        counter = 0

        for i in range(range_vector):
            if vector[i] == j:
                counter += 1def busca_repetidos(vector):
    moda = []
    for i in range(len(vector)):
        if not vector[i] in vector:
            moda.append(vector[i])
    return moda 

def nicole_code(vector):
    moda = []
    counter = 0
    a = None 
    elementos_nao_repetidos = busca_repetidos(vector)
    contador_el_repetidos = 0 
    index_el_repetido = 0 

    for el in elementos_nao_repetidos:
        counter_el = 0
        for i in range(vector):
            if vector[i] == el:
                counter_el += 1
                if counter_el > contador_el_repetidos:
                    contador_el_repetidos
                if counter > counter_of_most_repeated_element:
                    counter_of_most_repeated_element = counter
                    index_of_most_repeated_element = i

    return [counter_of_most_repeated_element, vector[index_of_most_repeated_element]]

print(most_repeated_element(test_vector)) 