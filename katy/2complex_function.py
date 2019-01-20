# You've got a task to change complex_function a little. The way it behaves if None is in objects list
# made whole system more reliable. Now we need the same behaviour for empty string in the list.
# Don't hurry. It's not very urgent. The part of system code that calls complex_function is here:
#   a = list(x)
#   b = dict(y)
#   complex_function(a, b)


def complex_function(objects, dict):
    list = []
    i = 0
    while i<len(objects):
        x = objects[i]
        i = i+1
        if not(x == None or x in dict.keys()) and x: #musi byc tutaj and !!! bo na pierwszy warunek '' zwroci true i wtedy bedzie append
                                                        # deMorgan Law
            list.append(x)
    x = set(list)
    return x

assert complex_function([1, None, 's', 2, 1, ''], {'s': 2, 2: 3}) == {1}


#REFACTOR

def complex_function_(elements, dictionary):
    return {e for e in elements if e and e not in dictionary.keys()}

assert complex_function_([1, None, 's', 2, 1, ''], {'s': 2, 2: 3}) == {1}
