def rotLeft(a, d):
    for i in range(d):
        a.append(a[0])
        a.pop(0)
    return a
