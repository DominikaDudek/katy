# Please write a function to verify anagrams, it should be case insensitive
# and ignoring spaces. An anagram is a word or phrase formed by rearranging
# the letters of a different word or phrase, typically using all the original
# letters exactly once.


def verify_anagrams(first_word, second_word):
    def lower_and_replace(word):
        word = word.lower()
        word = word.replace(" ", "")
        return word

    first_word = lower_and_replace(first_word)
    second_word = lower_and_replace(second_word)

    def sort_the_word(word):
        return ''.join(sorted(word))

    if sort_the_word(first_word) == sort_the_word(second_word):
        return True
    return False


assert verify_anagrams("Programming", "Gram Ring Mop") is True
assert verify_anagrams("hello", "Ole Oh") is False
assert verify_anagrams("Kyoto", "Tokyo") is True
assert verify_anagrams("Dalek", "Leak") is False
assert verify_anagrams("Named", "Maiden") is False


