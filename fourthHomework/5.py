from functools import reduce

lst = [el for el in range(100, 1001) if el % 2 == 0]
print(lst)
sum = reduce(lambda a, b: a + b, lst)
print(sum)
