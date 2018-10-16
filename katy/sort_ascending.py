def sort_array(source_array):
    array_of_even_and_indexes = []
    sorted_array = []
    if source_array:
        for index, element in enumerate(source_array):
            if not element % 2:
                array_of_even_and_indexes.append((index, element))
            else:
                sorted_array.append(element)
        sorted_array.sort()
        for pair in array_of_even_and_indexes:
            sorted_array.insert(pair[0], pair[1])

    return sorted_array


def wow(source_array):
    odds = sorted((x for x in source_array if x % 2), reverse=True)
    print odds
    print [x if x % 2 == 0 else odds.pop() for x in source_array]




assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
assert sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]
assert sort_array([]) == []