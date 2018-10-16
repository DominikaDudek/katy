def is_pangram(s):
    all_the_letters = 'qwertyuiopasdfghjklzxcvbnm'
    all_the_letters_sorted = "".join(sorted(all_the_letters))
    input_sorted = "".join(sorted(s.lower()))
    if input_sorted.endswith(all_the_letters_sorted):
        return True
    return False

pangram = "T quick, bwn fx jmps ver h lazy dog!"
assert is_pangram(pangram) is True