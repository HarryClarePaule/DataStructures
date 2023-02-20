def sum_list_high(lst):
    sums = [0] * len(lst)
    sums[0] = lst[0]
    for i in range(1, len(lst)):
        sums[i] = sums[i-1] + lst[i]
    return sums[-1]


def sum_list_low(lst):
    total = 0
    for num in lst:
        total += num
    return total
