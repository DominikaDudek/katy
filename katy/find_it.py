def find_it(seq):
    for elem in seq:
        if seq.count(elem) % 2:
            return elem




assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5