#1
def som_values(dct):
    total = 0 
    for i in dct:
        total += dct[i]
    return total

#2
def max_value(dct):
    max_key = None
    _max = 0
    for i in dct:
        if dct[i] > _max:
            _max = dct[i]
            max_key = i
    return max_key

#3
def count_characters(str):
    d = {}
    for i in str:
        if i not in d:
            d[i] = str.count(i)
    return d

#4
def invert_dict(dct):
    inverted = {}
    for i in dct:
        inverted[dct[i]] = i
    return inverted

#5
def merge_dict(dct1, dct2):
    merged = {}
    for  i in dct1:
        if i in dct2:
            continue
        merged[i] = dct1[i]
    for i in dct2:
        merged[i] = dct2[i]
    return merged

#6
def filter_by_value(dct, value):
    filtered = {}
    for i in dct:
        if dct[i] > value:
            filtered[i] = dct[i]
    return filtered

#7
def group_by_first_letter(lst):
    grouped = {}
    for i in lst:
        if i[0] in grouped:
            grouped[i[0]].append(i)
        else:
            grouped[i[0]] = [i]
    return grouped

#8
def word_frequency(str):
    frequency = {}
    words = str.split()
    for  i in words:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency

#9
def common_keys(dct1, dct2):
    common = []
    for i in dct1:
        if  i in dct2:
            common.append(i)
    return sorted(common)

#10
def most_frequent_value(dct):
    frequent_value = 0
    values = list(dct.values())
    for i in dct.values():
        if values.count(i) > frequent_value:
            frequent_value = values.count(i)
    return frequent_value



