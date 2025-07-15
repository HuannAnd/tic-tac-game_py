test_vector = [7, 19, 4, 10, 8, 1, 18, 6, 3, 12]


def selection_sort(vector):
    greater_element = vector[0]

    for i in range(1, len(vector) - 1):
        if greater_element < vector[i]:
            greater_element = vector[i]

    return greater_element


print(f"O maior elemento do vetor {test_vector} é o {selection_sort(test_vector)}")


def selection_sort_2(vector):
    def swap(vector, from_index, to_index):
        temp = vector[from_index]
        vector[from_index] = vector[to_index]
        vector[to_index] = temp

    def select_smallest(vector, start):
        smallest_index = start

        for i in range(start + 1, len(vector)):
            if vector[i] < vector[smallest_index]:
                smallest_index = i

        return smallest_index

    def sort(vector):
        for j in range(len(vector) - 1):

            smallest_index = select_smallest(vector, j)
            swap(vector, smallest_index, j)

    print("Vector before sort:")
    print(vector)
    print("Vector after sort")
    sort(vector)
    print(vector)

selection_sort_2(test_vector)