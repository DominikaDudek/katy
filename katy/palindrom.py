def longest_palindrome(input):
    if len(input) == 1 :
        return True
    elif not len(input):
        return False

    for index in xrange(len(input) / 2):
        if not input[index] == input[-(index+1)]:
            return False
    return True



assert longest_palindrome("a") is True
assert longest_palindrome("") is False
assert longest_palindrome("aa") is True
assert longest_palindrome("baab") is True
assert longest_palindrome("aab") is False
assert longest_palindrome("abcba") is True

