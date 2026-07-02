import gc


def f():
    for i in range(3):
        yield i


g = f()

for _ in range(3):
    print(next(g))
