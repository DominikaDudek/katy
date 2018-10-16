import math

def gap(g, m, n):

    def is_prime(number):
        if number == 1:
            return None
        if number == 2:
            return number
        if number > 2 and number % 2 == 0:
            return None
        sqrt_of_number = int(math.floor(math.sqrt(number)))

        for num in xrange(3, sqrt_of_number + 1, 2):
            if number % num == 0:
                return None
        return number

    list_of_primes = [elem for elem in xrange(m,n) if is_prime(elem)]

    if list_of_primes:
        for index in xrange(1,len(list_of_primes)):
            if list_of_primes[index] - list_of_primes[index - 1] == g:
                return [list_of_primes[index - 1], list_of_primes[index]]
    return None


assert gap(2,100,110) == [101, 103]
assert gap(4,100,110) == [103, 107]
assert gap(6,100,110) == None
assert gap(8,300,400) == [359, 367]
assert gap(10,300,400) == [337, 347]