number_of_coaches = int(input())
initial_order_coaches = [i + 1 for i in range(number_of_coaches)]
expected_permutation = list(map(int, input().split()))
print(initial_order_coaches)
print(expected_permutation)

[].sort()
def is_possible_perumutation(from_order, to_order):
    station_a = []
    station_b = []
    is_empty = False
    pointer_from = 0

    while not is_empty:
        for i in range(len(to_order)):
            if len(station_a) != 0 and station_a[-1] == to_order[pointer_from]:
                station_b.append(station_a.pop())
                pointer_from += 1
            elif from_order[i] == to_order[pointer_from]:
                station_b.append(from_order[i])
                pointer_from += 1
            else:
                station_a.append(from_order[i])
            from_order.pop()
            is_empty = len(from_order) == 0
            print(from_order)
            print(station_b)
  
    for j in range(len(station_a) - 1, 0, -1):
      if station_a[j] != to_order[pointer_from]:
        return False

    return True

message = "Yes" if is_possible_perumutation(initial_order_coaches, expected_permutation) else "No"
print(message)