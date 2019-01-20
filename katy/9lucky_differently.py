# Program to check if a given number is Lucky (all digits are different)
#
# A number is lucky if all digits of the number are different. How to check if a given number is lucky or not.
# Examples:
#
# Input: n = 983
# Output: true
# All digits are different
#
# Input: n = 9838
# Output: false
# 8 appears twice

def lucky(integer):
    to_string = str(integer)


assert lucky(983) == True
assert lucky(9838) == False