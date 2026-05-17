#1
def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

#2
def max_list(lst):
    if not lst:
        return None
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item
    return max_value

#3
def count_occurrences(lst, value):
    count = 0
    for item in lst:
        if item == value:
            count += 1
    return count

#4
def reverse_list(lst):
    new_list = []
    for i in range(len(lst)):
        new_list.append(lst.pop())
    return new_list

#5
def remove_duplicates(lst):
    new_list = []
    for i in lst:
        if i in new_list:
            continue
        new_list.append(i)
    return new_list

#6
def seconde_largest(lst):
    if len(lst) < 2:
        return None
    largest = 0
    _seconde_largest = 0
    for i in lst:
        if i >= largest:
            _seconde_largest = largest
            largest = i
        elif largest > i > _seconde_largest:
            _seconde_largest = i
    if largest == _seconde_largest:
        return None
    return _seconde_largest

#7
def marge_lists(lst1, lst2):
    merged = []
    i = 0
    j = 0
    len1, len2 = len(lst1), len(lst2)
    while i < len1 and j < len2:
        if lst1[i] <= lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])
    return merged


#8
def rotate_list(lst, n):
    if n > len(lst):
        n -= len(lst)
    n = len(lst) - n
    return lst[n:] + lst[:n]


