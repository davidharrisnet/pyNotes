def lists():
    print("list")
    f = ["a","b"]
    g = [1, "c"]
    print(g)
    g[0] = "c"
    print(g)
    if "a" in f:
        print("found 'a'")

def tuples():
    print("tuple")
    f = (1,2,3)
    g = { 1, "c"}
    print(g)
    # g[0] = "c" -- error
    # print(g)
    if "c" in g:
        print("found 'c'")

def sets():
    print("sets")
    f = { 1,2,3,3,4}
    print(f)

def dicts():
    dict = {
        "a": "alphabet",
        "b": "bottles",
        "c": "cards"
    }
    print(dict)

# dicts()

def lists():
    p = [('a',1), ('b',2), ('c',3)]
    letter, numbers =  zip(*p)




x = 2;

def changeX():
    x = 4

def changeX2():
    global x
    x = 5


changeX()
print(x)
changeX2()
print(x)