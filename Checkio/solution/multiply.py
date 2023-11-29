from operator import mul as mult_two
from typing import Any


class Multiply:
    __a = 2
    __b = 5

    @classmethod
    def func(cls) -> Any:
        return mult_two(cls.__a, cls.__b)


print(Multiply.func())
