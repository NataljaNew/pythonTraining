def inversions(sequence):
    count = 0
    index = 1
    for el in sequence:
        for e in sequence[index:]:
            if el > e:
                count += 1
        index += 1
    return count


print(inversions(([3, 1, 4, 2])))
