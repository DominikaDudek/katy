def last_digit(n1, n2):
    calcuate = n1 ** n2

    return calcuate % 10



assert last_digit(4, 1) ==  4
assert last_digit(4, 2) ==  6
assert last_digit(9, 7) == 9
assert last_digit(10, 10 ** 10) == 0
assert last_digit(2 ** 200, 2 ** 300) == 6
assert last_digit(3715290469715693021198967285016729344580685479654510946723,
                                  68819615221552997273737174557165657483427362207517952651) == 7


# efficient shit

# def last_digit(n1, n2):
#     return pow( n1, n2, 10 )