def wave(string):
    # array = []
    # if string:
    #     for index in xrange(len(string)):
    #         if not string[index].isspace():
    #             array.append(string[0:index] + string[index].capitalize() + string[index + 1:])
    # # return array

    return [string[0:index] + string[index].capitalize() + string[index + 1:] for index in xrange(len(string)) if not string[index].isspace()]


assert wave("two words") == ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs",
                             "two wordS"]
assert wave(" gap ") == [" Gap ", " gAp ", " gaP "]
assert wave("") == []
assert wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
