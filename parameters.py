def dict(**dict):
    print(type(dict))
    for d in dict:
        print(d, ":", dict[d])

# dict(a="alphabet", b="bottles")

def list(*list):
    print(type(list))
    for i in list:
        print(i)
# list("a","b","c")


def add(*n):
    for i in n:
        print(i)

# add(1,2,3)


def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x + 1

g = doubler(f1)


print(g(2))
