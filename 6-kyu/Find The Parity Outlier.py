def find_outlier(integers):
    count_odd = 0
    count_even = 0
    
    for i in integers:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    
    if count_even == 1:
        return list(filter(lambda x: x % 2 == 0, integers))[0]
    elif count_odd == 1:
        return list(filter(lambda x: x % 2 != 0, integers))[0]
    
