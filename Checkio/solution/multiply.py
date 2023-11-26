from operator import mul as mult_two


class Multiply:
    __a = 2
    __b = 5

    @classmethod
    def func(cls) -> int:
        return mult_two(cls.__a, cls.__b)


print(Multiply.func())
