def anagrams2(word, words):
    accumulate_anagrams = []

    def sort_the_word(word):
        return "".join(sorted(word))

    for w in words:
        if sort_the_word(word) == sort_the_word(w):
            accumulate_anagrams.append(w)

    return accumulate_anagrams

def anagrams(word, words):
    return [w for w in words if sorted(word) == sorted(w)]



assert anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']

a = [[1,2], [3, 4]]
k = [inner for outer in a for inner in outer]