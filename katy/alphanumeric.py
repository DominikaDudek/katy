def alphanumeric(string):

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'w', 'v', 'y', 'z']

    if string:
        for element in string:
            if element.lower() not in letters:
                try:
                    int(element)
                except ValueError:
                    return False
        return True
    return False


def alphanumeric2(string):

    allowed = '1234567890qwertyuiopasdfghjklzxcvbnm'

    for element in string.lower():
        if element not in allowed:
            return False
    return True


# The string has the following conditions to be alphanumeric:
#
# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces/underscore

assert alphanumeric2("hello_world") is False
assert alphanumeric2("PassW0rd") is True
assert alphanumeric2("     ") is False
assert alphanumeric2("a") is True
