def smallest(n):
    as_string = str(n)
    sorted_n = "".join(sorted(as_string))
    smallest_number = sorted_n[0]
    index_to_remove = as_string.index(smallest_number)
    number_without_the_smallest = as_string[:index_to_remove] + as_string[index_to_remove + 1:]
    all_the_possibilities = []

    pass




    # return [number, index_to_remove, index_to_insert]


assert smallest(261235) == [126235, 2, 0]
assert smallest(209917) == [29917, 0, 1]
assert smallest(285365) == [238565, 3, 1]
assert smallest(269045) == [26945, 3, 0]
assert smallest(296837) == [239687, 4, 1]