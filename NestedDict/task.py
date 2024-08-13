def pluck(data, path, default=None):
    keys = [key for key in path.split('.')]
    for k in keys:
        try:
            data = data.get(k, default)
        except:
            data = default
    return data




