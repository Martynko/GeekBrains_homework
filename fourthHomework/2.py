
def my_generator(lst):
    last = lst[0]

    for el in lst:
        if(el > last):
            yield el
        last = el


lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_lst = [el for el in my_generator(lst)]
print(new_lst)
