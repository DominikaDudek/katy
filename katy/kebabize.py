# def kebabize(string):
#     result = []
#     for index, letter in enumerate(string):
#         if letter.isupper():
#             if not result:
#                 result.append(letter.lower())
#             else:
#                 result.extend(['-', letter.lower()])
#         elif letter.isdigit():
#             continue
#         else:
#             result.append(letter)
#     return ''.join(result)


def kebabize(string):
    return ''.join(c if c.islower() else '-' + c.lower() for c in string if c.isalpha()).strip('-')


assert kebabize('myCamelCasedString') == 'my-camel-cased-string'
assert kebabize('myCamelHas3Humps') == 'my-camel-has-humps'
assert kebabize('SOS') == 's-o-s'
assert kebabize('42') == ''
assert kebabize('CodeWars') == 'code-wars'