# Szyfr podstawieniowy.
# Input: string do zaszyfrowania oraz klucz w postaci dicta gdzie key to literka zastepowane przez literkę value. Literki, ktore nie są zdefiniowane jako key w dikcie nie są zastepowane.
# Np.:
# Input:
# „i am pretty”, {‘a’: ‘e’, ‘e’: ‘b’, ‘m’: ‘x’}
# Output:
# “I ex prbtty”


def decode(phrase, cipher):
    result = []
    for letter in phrase:
        if letter in cipher:
            result.append(cipher[letter])
        else:
            result.append(letter)
    return ''.join(result)


assert decode('is me', {'s': 'k'}) == 'ik me'
