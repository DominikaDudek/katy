def make_readable(seconds):
    seconds_ind_minute = 60
    seconds_in_hour = 3600
    how_many_hours = seconds / 3600
    how_much_is_left_after_hours = seconds - how_many_hours * seconds_in_hour

    how_many_minutes = how_much_is_left_after_hours / seconds_ind_minute

    how_many_seconds = how_much_is_left_after_hours - seconds_ind_minute * how_many_minutes

    readable = "{hours}:{minutes}:{seconds}"

    print readable.format(hours=count_wholes(how_many_hours),
                          minutes=count_wholes(how_many_minutes),
                          seconds=count_wholes(how_many_seconds))

def count_wholes(number):
    if number // 1 >= 10:
        return number
    return '0' + str(number)


make_readable(0) # "00:00:00")
make_readable(5) #, "00:00:05")
make_readable(60) #"00:01:00")
make_readable(86399)  #"23:59:59")
make_readable(359999) # "99:59:59")