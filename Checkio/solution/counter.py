from collections import Counter, defaultdict, namedtuple
from itertools import chain
from typing import Iterable


class CounterDefault:
    @staticmethod
    def count(args):
        raise NotImplementedError


class CounterCollection(CounterDefault):
    @staticmethod
    def count(args) -> Counter:
        return Counter(args)


class DefaultDict(CounterDefault):
    @staticmethod
    def count(args) -> defaultdict.items:
        counter = defaultdict(int)
        for k in args:
            counter[k] += 1
        return counter.items()


if __name__ == "__main__":
    args_one = (i for i in range(10))
    args_two = (j for j in range(5))
    args_chain = chain(args_one, args_two)
    c_counter = CounterCollection.count(args_chain)
    d_counter = DefaultDict.count(args_chain)

