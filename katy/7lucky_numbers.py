#You should keep all the values generated during the process


def is_happy_number(n):
    visited = set()
    visited.add(n)

    def convert_to_string_and_return_square(integer):
        to_string = str(integer)
        accumulate = 0
        for element in to_string:
            accumulate += int(element) ** 2
        return accumulate

    a = convert_to_string_and_return_square(n)
    visited.add(a)
    while a != 1:
        a = convert_to_string_and_return_square(a)
        if a in visited:
            return False
        if a == 1:
            return True
        visited.add(a)


assert is_happy_number(7) is True
assert is_happy_number(9) is False
assert is_happy_number(137) is False
assert is_happy_number(3319) is True
assert is_happy_number(10845) is False

# Clarification example. 19 is a happy number because:
# 1 ** 2 + 9 ** 2 = 82
# 8 ** 2 + 2 ** 2 = 68
# 6 ** 2 + 8 ** 2 = 36 + 64 = 100
# 1 ** 2 + 0 ** 2 + 0 ** 2 = 1
