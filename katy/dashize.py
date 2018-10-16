def dashatize(num):
    result = ""
    if num:
        for elem in str(abs(num)):
            if int(elem) % 2:
                result += '-' + elem + '-'
            else:
                result += elem
        return result.replace('--', '-').strip('-')
    return str(num)


assert dashatize(274) == "2-7-4"
assert dashatize(5311) == "5-3-1-1"
assert dashatize(86320) == "86-3-20"
assert dashatize(974302) == "9-7-4-3-02"
assert dashatize(None) == "None"
assert dashatize(0) == "0"
assert dashatize(-1) == "1"
assert dashatize(-28369) == "28-3-6-9"