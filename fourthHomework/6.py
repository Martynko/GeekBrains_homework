from itertools import count
from itertools import cycle


def count_test(start, num=10):
    i = 0
    c = count()
    while i < num:
        i += 1
        yield c.__next__() + start


def cycle_test(lst, times=1):
    if(times < 1):
        return

    c = cycle(lst)
    iter_count = (int)(len(lst)) * times
    i = 0
    while i < iter_count:
        i += 1
        yield c.__next__()


count_lst = [el for el in count_test(5)]
print(count_lst)

test_lst = [1, 2, 3, 4, 5]
cycle_lst = [el for el in cycle_test(test_lst, 3)]
print(cycle_lst)
