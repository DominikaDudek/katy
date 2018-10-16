def increment_string(strng):
    integer_counter = 0
    letters_counter = 0
    for let in strng:
        try:
            int(let)
            integer_counter += int(let)
            letters_counter += 1
        except ValueError:
            continue
    if integer_counter:
        return strng[:-letters_counter] + str(integer_counter + 1)
    else:
        return strng + '1'

a  = increment_string("foobar001")
print a