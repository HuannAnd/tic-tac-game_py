import itertools

tests_sort_results = itertools.permutations([1, 2, 3, 4, 5])


def define_list_of_elements():
    list = []

    for i in range(5):
        print("Digite um numero")
        num = float(input())
        list.append(num)

    return list


def read_num():
    return float(input())


def sort_elements2(elements):
    a = elements[0]
    b = elements[1]
    c = elements[2]
    d = elements[3]
    e = elements[4]

    if b > a:
        a, b = b, a
    if c > b:
        b, c = c, b
    if c > a:
        a, c = c, a

    if (a > b) and (b > d) and (a > c):
        if c > d:
            if c > e:
                if d > e:
                    return (e, d, c, b, a)
                return (d, e, c, b, a)
            return (d, c, e, b, a)
        else:
            if b > e:
                if d > e:
                    if c > e:
                        return (e, c, d, b, a)
                    return (c, e, d, b, a)
                return (c, d, e, b, a)
            else:
                if a > e:
                    return (c, d, b, e, a)
                return (c, d, b, a, e)
    else:
        if a > d:
            if d > e:
                if b > e:
                    if c > e:
                        return (e, c, b, d, a)
                    return (e, c, b, d, a)

def sort_elements1(elements):
    counter = 0

    def switch_elements(index_1, index_2):
        nonlocal counter
        nonlocal elements

        counter += 1

        if elements[index_1] > elements[index_2]:
            elements[index_1], elements[index_2] = elements[index_2], elements[index_1]
            counter += 1

    switch_elements(0, 1)
    switch_elements(2, 3)
    switch_elements(0, 2)
    switch_elements(1, 3)
    switch_elements(1, 4)
    switch_elements(2, 4)
    switch_elements(1, 2)

    return elements


def test_algorithm():
    global tests_sort_results
    cases_counter = 0
    expected_permutation = (1, 2, 3, 4, 5)
    print(tests_sort_results)

    for test_case in tests_sort_results:
        print(test_case)
        final_permutation = sort_elements2(test_case)
        print(final_permutation)

        if final_permutation == expected_permutation:
            cases_counter += 1

    diagnostic = "%s Casos que deram %s" % (cases_counter, expected_permutation)
    print(diagnostic)


# test_algorithm()
# result = sort_elements1([2, 1, 3, 5, 4])
# print(result)
# print(sort_elements2([1, 4, 3, 2, 5]))
print(test_algorithm())
