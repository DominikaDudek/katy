# Input: two lists of integers (there might be duplicates)
# Output: True if for each element of the first list there's a corresponding
#         square of it in the second one.

def has_corresponding_squares(first_argument, second_argument):
    squared = [element ** 2 for element in first_argument]
    return sorted(squared) == sorted(second_argument)
    # for element in first_argument:
    #     if not(element**2 in second_argument) or len(first_argument) != len(second_argument):
    #         return False
    # return True

assert has_corresponding_squares([1, 2, 3], [1, 4, 9]) is True
assert has_corresponding_squares([1], [1, 5]) is False
assert has_corresponding_squares([2, 2, 4, 4], [16, 4, 4, 16]) is True
assert has_corresponding_squares([2], [4, 4]) is False
