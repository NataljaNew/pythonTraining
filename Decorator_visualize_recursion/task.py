import functools


def recviz(func):
    func.recursion_counter = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # val = func(*args, **kwargs)
        argstr = ', '.join(
            [repr(a) for a in args] +
            ["%s=%s" % (a, repr(b)) for a, b in kwargs.items()])
        tab = '    ' * func.recursion_counter
        func.recursion_counter += 1
        print(f'{tab}-> {func.__name__}({argstr})')
        temp = func(*args,**kwargs)
        func.recursion_counter -= 1
        print(f'{tab}<- {repr(temp)}')
        return temp
    return wrapper


@recviz
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(4)
