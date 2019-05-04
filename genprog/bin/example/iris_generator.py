
import iris_data as dat
import feature as ft

import random

def gt(x,y):
    return x > y

def lt(x,y):
    return x < y

comparators = [gt,lt]

max_float = 7
def ran_value():
    return random.random() * max_float

chars = range(4)

class Generator:

    def __init__(self, prob_float, max_depth):
        self._prob_float = prob_float
        self._max_depth = max_depth

    def random_gene(self):
        return ft.Strategy([self._comparison() for _ in range(random.randint(1,self._max_depth))])

    def _comparison(self):
        if (random.random() < self._prob_float):
            return self._float_comparison()
        else:
            return self._val_comparison()

    def _float_comparison(self):
        return ft.Feature(random.choice(chars),ran_value(),random.choice(comparators),f_type="float")

    def _val_comparison(self):
        choices = random.sample(chars,2)
        return ft.Feature(choices[0],choices[1],random.choice(comparators),f_type="char")

