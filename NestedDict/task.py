def pluck(data, path, default=None):
    keys = [key for key in path.split('.')]
    for k in keys:
        try:
            data = data.get(k, default)
        except:
            data = default
    return data



d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'c.d'))
