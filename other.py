

def other(i):
    if (i == 2):
        pass
    else:
        print("not 2")


other(2)


def pizza(cheese:str) -> int:
    print(type(cheese))
    print(pizza.__annotations__)
    return cheese


import builtins

l = dir(builtins)

print(type(l))

for i in l:
    print(i)


print (builtins.map)


def make_multiplier(n):
    return lambda x: x * n

f = make_multiplier(3)



print(f)
print(f(2))

numbers = (1,2,3,4)

def add(n):
    return n + n


m = map(add,numbers)

# print(list(m))


