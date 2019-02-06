def is_prime(number):

    if number < 2:
        return False

    for n in range(1, number):
        if number % n == 0:
            return False

    return True



print is_prime(6172344)
