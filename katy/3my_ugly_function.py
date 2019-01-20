# Refactor my_ugly_function into a pretty one while keeping its original purpose.
# You may rename the input arguments if you wish.

random_objects = ['foo', 'bar', 'fizz', 'buzz', None, False]
random_dict = {'foo': 1, 'fizz': None}


def my_ugly_function(objects, dict):
    list = []
    for x in objects:
        if not(x == None or x in dict.keys()):
            list.append(x)
    x = set(list)
    return x


def my_pretty_function(elements, dict):
    return {element for element in elements if element != None  and element not in dict.keys()}

#odsiewamy tylko None, a nie FALSE, ma on zostac dlatego jest !=None

#In [20]: print None or False
#-------> print(None or False)
#False

#In [21]: print False or None
#-------> print(False or None)
#None


#The "or" operator returns the value of its first operand,
# if that value is true in the Pythonic boolean sense (aka its "truthiness"),
# otherwise it returns the value of its second operand, whatever it happens to be.
# ale jak mamy w ifie cos tam jest false or cos tam jest false to nie zwroci nam tego durgiego false'a,
# tylko obliczy i nie wejdzie do petli ifa

assert {'bar', 'buzz', False} == my_ugly_function(random_objects, random_dict)
assert {'bar', 'buzz', False} == my_pretty_function(random_objects, random_dict)