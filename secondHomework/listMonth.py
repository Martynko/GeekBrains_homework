def list_month():
    monthes_lst = ['winter', 'spring', 'summer', 'autumn']
    month_num = int(input('enter month number: '))
    index = int(month_num % 12 // 3)
    print(monthes_lst[index])


list_month()
