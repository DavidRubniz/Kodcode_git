#1
def sum_of_tuple(tpl):
    total = 0
    for i in tpl:
        total += i
    return total

#2
def maximum_element(tpl):
    _max = 0
    for i in tpl:
        if i > _max:
            _max = i
    return _max

#3
def count_occurrences(tpl, value):
    count = 0 
    for i in tpl:
        if i == value:
            count += 1
    return count

#4
def revers_tuple(tpl):
    new_tuple = []
    for  i in range(1, len(tpl) +1):
        new_tuple.append(tpl[-i])
    return tuple(new_tuple)

#5
def swap_pairs(tpl):
    new_tuple = []
    for i in range(0, len(tpl), 2):
        new_tuple.append(tpl[i + 1])
        new_tuple.append(tpl[i])
    return tuple(new_tuple)

#6
def min_max(tpl):
    _min, _max = 0,0
    for i in tpl:
        if i > _max:
            _max = i
        if i < _min:
            _min = i
    return (_min, _max)

#7
def distance(tpl1, tpl2):
    x1, x2 = tpl1
    y1, y2 = tpl2
    return (((x2 - x1) **2) + ((y2 - y1) ** 2)) ** 0.5

#8
def marge_and_sort(tpl1, tpl2):
    merged = list(tpl1+ tpl2)
    n = len(merged)
    for i in range(n):
        for j in range(0, n-i-1):
            if merged[j] > merged[j+1]:
                merged[j], merged[j+1] = merged[j+1], merged[j]
    return tuple(merged)

#9
def frequency_table(tpl):
    new_tuple = []
    already_seen = []
    for i in tpl:
        if i in already_seen:
            continue
        new_tuple.append((i, tpl.count(i)))
        already_seen.append(i)
    return tuple(new_tuple)

#10
def rotate_tuple(tpl, k):
    k = k % len(tpl)
    k = len(tpl) - k
    return tuple(list(tpl[k:] + tpl[:k]))
print(rotate_tuple((1,2,3,4,5), 2))
