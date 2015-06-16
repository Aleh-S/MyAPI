from random import randint

def create_random_list(n=None, range_min=None, range_max=None):
    if n is None:
        n = 500
    if range_min is None:
        range_min = 0
    if range_max is None:
        range_max = 20
    return [randint(range_min, range_max) for p in range(n)]

# l =[randint(0, 20) for p in range(500)]
# print l


print create_random_list()

