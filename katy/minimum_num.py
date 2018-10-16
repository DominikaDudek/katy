import math


def minimum_number(numbers):
    sum_of_list = sum(numbers)

    def check_for_prime(number):
        if number == 1 or number == 2:
            return True
        if not number % 2:
            return False
        max_divisor = int(math.floor(math.sqrt(number)))
        for element in xrange(3, max_divisor + 1, 2):
            if not number % element:
                return False
        return True

    while not check_for_prime(sum_of_list):
        sum_of_list += 1

    return sum_of_list - sum(numbers)



assert minimum_number([3,1,2]) == 1
assert minimum_number([5,2]) == 0
assert minimum_number([1,1,1]) == 0
assert minimum_number([2,12,8,4,6]) == 5
assert minimum_number([50,39,49,6,17,28]) == 2
