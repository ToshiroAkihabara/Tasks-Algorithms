from operator import mul as mult_two
import numpy


def func(a: int, b: int):
    return mult_two(a, b) 

def func1(a: int, b: int):
    return numpy.prod([a,b])

func2 = lambda a, b: a * b

a = 2
b = 5

print(func(a, b))
print(func1(a, b))
print(func2(a, b))
