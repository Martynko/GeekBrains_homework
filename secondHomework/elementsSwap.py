def elements_swap():
    lst = input('please input data :').split()
    i = 0
    while i < len(lst) - 1:
        tmp = lst[i]
        lst[i] = lst[i+1]
        lst[i+1] = tmp
        i += 2
    print(lst)


elements_swap()
