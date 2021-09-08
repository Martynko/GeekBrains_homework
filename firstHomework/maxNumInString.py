def max_num_in_string():
    user_input = input('input some string containing only numbers: ')
    i = 0
    largest = 0
    while i < len(user_input):
        num = int(user_input[i])
        largest = num if largest < num else largest
        i += 1
    print('largest number in string is {}'.format(largest))


max_num_in_string()
