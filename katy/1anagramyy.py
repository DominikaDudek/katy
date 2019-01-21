# Please write a function to verify anagrams, it should be case insensitive
# and ignoring spaces. An anagram is a word or phrase formed by rearranging
# the letters of a different word or phrase, typically using all the original
# letters exactly once.


def verify_anagrams(first_word, second_word):
    def join_the_words(word):
        joined_word = ''.join(word.replace(' ', ''))
        lower_case_word = joined_word.lower()
        return lower_case_word

    # return sorted(''.join(first_word.replace(' ', '')).lower()) == sorted(''.join(second_word.replace(' ', '')).lower())

    return sorted(join_the_words(first_word)) == sorted(join_the_words(second_word))

assert verify_anagrams("Programming", "Gram Ring Mop") is True
assert verify_anagrams("hello", "Ole Oh") is False
assert verify_anagrams("Kyoto", "Tokyo") is True
assert verify_anagrams("Dalek", "Leak") is False
assert verify_anagrams("Named", "Maiden") is False
