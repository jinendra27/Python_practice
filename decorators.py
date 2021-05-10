def decor(fun):
    def inner():
        value = fun()
        return value + 15000
    return inner

def decor2(fun):
    def inner():
        value = fun()
        return value - 0.12 * value
    return inner

@decor
def e1():
    return 120000

print(e1())

@decor
def e2():
    return 240000

print(e2())
