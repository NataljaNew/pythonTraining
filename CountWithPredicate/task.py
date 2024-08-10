def quantify(iterable, predicate):
    if not predicate:
        predicate = bool
    result = sum([1 for el in iterable if predicate(el)])
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(quantify(numbers, lambda x: x % 2 == 0))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(quantify(numbers, lambda x: x > 1))
