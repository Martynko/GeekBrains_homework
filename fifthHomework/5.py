import random
from functools import reduce


def fill_file(file_path, num_count):
    with open(file_path, 'w') as file:
        file.write(''.join(str(n) + ' '
                   for n in random.sample(range(0, num_count * 2), num_count)))
        file.flush()


def sum_in_file(file_path):
    with open(file_path, 'r') as file:
        nums = [int(n) for n in file.readline().split()]
        print('sum of numbers in file {}'.format(
            reduce(lambda a, b: a + b, nums)))


fill_file('fifthFile.txt', 200)
sum_in_file('fifthFile.txt')
