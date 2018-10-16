# def move_zeros(array):
#     zeros_counter = 0
#     new_list = []
#     for element in array:
#         if element == 0 and type(element) != bool:
#             zeros_counter += 1
#         else:
#             new_list.append(element)
#     new_list.extend([0] * zeros_counter)
#
#     return new_list


def move_zeros(array):
    a = sorted(array, key=lambda x: x == 0 and type(x) != bool)
    return a


# To explain a little: sorted() will sort an iterable of inputs (in this case, array), by whatever metric you define. If you gave it a list of ints and didn't tell it how to sort, it would sort them as you'd expect - smallest first.
#
# However, you can tell sorted() what you want to sort by, with the key argument. key must be a function that returns something orderable.
#
# In this case, our function to sort by is a lambda function, which is just a shorthand way of writing a function inline. What does this function do? It returns True if x==0 and type(x) is not bool. So, all your 0s and 0.0s (and complex 0i + 0js? I don't know about those enough) will return True, while everything else - any non-zero int, or any str will return False. Also, False will return False, because even though False == 0, type(False) is bool.
#
# Alright, so we've got a bunch of True/False values as our key outputs... how the heck does the rest of this work?!
#
# Well, now we sort by the keys. Since False is equivalent to 0 and True is equivalent to 1, we put all of our False before all of our True. This means we put all of our (int, or str, or False) before all of our (0 or 0.0 or 0i + 0j).
#
# Ok, fine, but how come it doesn't screw up the order of things? If I sort (3, 2, 1) by their keys (True, True, True) why do I get (3, 2, 1) back out? Because Python's sort is a stable sort. That means, if two items compare equal, the first one in is the first one out. So, everything that gets a False stays in order, and everything that was True (aka 0-ish) stays in order; but all the False come before all the True.


assert move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]) == [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
assert move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]) == ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]

print move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])

assert move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]) == ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]
assert move_zeros([1,2,0,1,0,1,0,3,0,1]) == [ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ]
assert move_zeros([0,1,None,2,False,1,0]) == [1,None,2,False,1,0,0]
assert move_zeros(["a","b"]) == ["a","b"]
assert move_zeros(["a"]) == ["a"]
assert move_zeros([0,0]) == [0,0]
assert move_zeros([0]) == [0]
assert move_zeros([]) == []

