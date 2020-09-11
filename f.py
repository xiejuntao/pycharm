from abstest import  my_abs
from abstest import a
from functools import reduce
print(my_abs(-23))
a()

L = list(range(100))
print(L[2:7])

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

def fuck(x):
    return 2 * x

r = map(fuck, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

def add(x,y):
    return x + y

print(reduce(add,[12,23,34]))