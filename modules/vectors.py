from typing import List
import numpy as np
Vector = List[float]

h = [0, 7,1,4]
print("h: " + str(h))
g = [9,8,7,6]
print("g : " + str(g))
print("")
print("zip(h,g)")
z = zip(h,g)

for zi in z:
    print("z: " + str(zi))
print("s")
s = [i * j for i,j in zip(h,g)]
print(s)

print("")
a = np.array(h)
b = np.array(g)
z = zip(a,h)

print(a * b)

print(np.multiply(a,b))

print(a + 2)