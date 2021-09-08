def strange_sum():
    user_input = input('input a number: ')
    result = float(user_input) + float(user_input*2) + float(user_input*3)
    print('result is {}'.format(result))


strange_sum()
