
def list_of_lists(lis):
    # a = []
    # for inner in lis:
    #     for element in inner:
    #         a.append(element)
    # return a
    return [element for inner in lis for element in inner]

# zobacz sobie to tak, zwroc nam element dlatego rozpoczynamy od slowa element a element to 1, 2,3 itd. nastepnie
# poiteruj sie po listch wewnwetrznych i po elemntach w tych listach wenetrznych,
#  masz dokladnie dwie te same petle napisane tylko w jednej linie

assert list_of_lists([[1,2,3], [5,6]]) == [1,2,3,5,6]