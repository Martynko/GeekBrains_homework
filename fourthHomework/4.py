def my_gen(lst):
    returned_elements = [lst[0]]
    for el in lst:
        if(not el in returned_elements):
            returned_elements.append(el)
            yield el


lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
filtered_lst = [el for el in my_gen(lst)]
print(filtered_lst)
