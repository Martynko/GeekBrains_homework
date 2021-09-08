def raiting():
    number_lst = [7, 5, 3, 3, 2]
    new_num = int(input('input a number: '))
    i = 0
    while True:
        if new_num > number_lst[i]:
            number_lst.insert(i, new_num)
            break
        i += 1
    print(number_lst)


raiting()
