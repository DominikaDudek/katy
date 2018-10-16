"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_list = []
    for index, element in enumerate(line):
        if new_list:
            if element == new_list[-1] and index != 0 and element != line[index - 1]:
                new_list[-1] = element * 2
            elif element != 0:
                new_list.append(element)
        elif element != 0:
            new_list.append(element)
    if len(line) != len(new_list):
        len_to_apen = len(line) - len(new_list)
        new_list.extend([0] * len_to_apen)

    return new_list

print merge([8,8])
print merge([0,0,2])
print merge([4,4,8])