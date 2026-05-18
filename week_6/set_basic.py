#1
def remove_duplicates(lst):
    new_list = list(set(lst))
    return new_list

#2
def count_unique_elemments(lst):
    new_list = []
    for i in lst:
        if i in new_list:
            continue
        new_list.append(i)
    return len(new_list)

#3
def common_elements(lst1, lst2):
    common = []
    for i in lst1:
        if i in lst2:
            common.append(i)
    return sorted(common)

#4
def lelement_in_only_one(lst1, lst2):
    unique = []
    for i in lst1:
        if i not in lst2:
            unique.append(i)
    for i in lst2:
        if i not in lst1:
            unique.append(i)
    return sorted(unique)

#5
def is_subset(lst1, lst2):
    for i in lst1:
        if i not in lst2:
            return False
    return True
def is_subset(lst1, lst2):
    return set(lst1) <= set(lst2)

#6
def unique_characters(str):
    ll = str.split('')
    return ll == list(set(ll))

#7
def first_repeated_element(lst):
    first_repeat = None
    for i in lst:
        if lst.count(i) > 1:
            first_repeat = i
            break 
    return first_repeat

#8
def distinct_words(str):
    words = str.split()
    return len(set(words))

#9
def pair_sum_exists(lst, target):
    seen = set()
    for i in lst:
        comp = target - i
        if comp in seen:
            return True
        seen.add(i)
    return False

#10
def symmetric_difference(lst1, lst2):
    unique = []
    for i in lst1:
        if i not in lst2:
            unique.append(i)
    for i in lst2:
        if i not in lst1:
            unique.append(i)
    return sorted(unique)

