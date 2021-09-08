def dict_month():
    monthes_dict = {
        1: 'winter',
        2: 'winter',
        3: 'spring',
        4: 'spring',
        5: 'spring',
        6: 'summer',
        7: 'summer',
        8: 'summer',
        9: 'autumn',
        10: 'autumn',
        11: 'autumn',
        12: 'winter',
    }
    month_num = int(input('enter month number: ')) % 12
    print(monthes_dict[month_num])


dict_month()
