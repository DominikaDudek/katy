# Please transform list of dicts to the dict of lists. For now let's assume
# that all dicts have the same set of keys. What if they could have different
# sets of keys?
from collections import defaultdict

def transform(input_list):
    # new_dict = dict()
    # for element in input_list:
    #     for key, value in element.iteritems():
    #         new_dict.setdefault(key, list())
    #         new_dict[key].append(value)
    # return new_dict
    # print {k: [dic[k] for dic in input_list] for k in input_list[0]}
    defalut = defaultdict(list)
    for dd in input_list:
        for k,v in dd.items():
            defalut[k].append(v)

    a = {defalut[k].append(v) for dd in input_list for k,v in dd.items()}
    return a


# The method setdefault() is similar to get(), but will set dict[key]=default if key is not already in dict.

# assert transform([]) == {}
# assert transform([{'a': 1}]) == {'a': [1]}
# assert transform([{'a': 1}, {'a': 2}]) == {'a': [1, 2]}
assert transform([{'a': 1, 'b': 3}, {'a': 2, 'b': 4}, {'c': 4}]) == {'a': [1, 2], 'b': [3, 4], 'c': [4]}
assert transform([{'a': 1}, {'a': 2}, {'a': 3}]) == {'a': [1, 2, 3]}
