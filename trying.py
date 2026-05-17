def ggg(r):
    counter = len(r)
    while counter > 0:
        _min = min(r)
        min_in = r.index(_min)
        _max = _min
        for i in range(min_in, len(r)):
            if r[i] > _max:
                _max = r[i]
        if _max > _min:
            return _max - _min
        else:
            r.remove(_min)
        counter -= 1
    return 0

print(ggg([5,5]))



