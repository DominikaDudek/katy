"""
Implement the function get_element_that_appears_odd_number_of_times which, given an iterable of hashable elements,
returns the element which appears in it an odd number of times (any of those if there are multiple)
"""


def get_element_that_appears_odd_number_of_times(iterable):
    for element in iterable:
        if iterable.count(element) % 2:
            return element



assert get_element_that_appears_odd_number_of_times([1, 2, 3, 4, 4, 3, 2, 1, 1]) == 1
assert get_element_that_appears_odd_number_of_times([1, 2, 3, 4, 4, 3, 2, 3, 1]) == 3
#assert get_element_that_appears_odd_number_of_times(iter([1, 2, 3, 4, 4, 3, 2, 1, 1])) == 1