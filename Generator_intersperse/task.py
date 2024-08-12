def intersperse(iterable, delimiter):
    if not iterable:
        return
    iterable = iter(iterable)
    yield next(iterable)
    for element in iterable:
        yield delimiter
        yield element


iterable = iter('Beegeek')

print(*intersperse(iterable, '+'))
