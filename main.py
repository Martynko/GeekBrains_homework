def first_exercise():
    number_input = float(input('input some number: '))
    print(number_input)
    string_input = input('input some string: ')
    print(string_input)


def seconds_convert():
    seconds = float(input('input seconds: '))
    print('{}:{}:{}'.format(int(seconds // 3600), int(seconds % 3600//60), int(seconds % 60)))


def strange_sum():
    user_input = input('input a number: ')
    result = float(user_input) + float(user_input*2) + float(user_input*3)
    print('result is {}'.format(result))


def max_num_in_string():
    user_input = input('input some string containing only numbers: ')
    i = 0
    largest = 0
    while i < len(user_input):
        num = int(user_input[i])
        largest = num if largest < num else largest
        i += 1
    print('largest number in string is {}'.format(largest))

def intake_calculator():
    intake = float(input('please enter business intake: '))
    expenses = float(input('please enter business expenses: '))

    if intake <= expenses:
        print('business earned no profit')
    else:
        print('profitability of proceeds {}'.format(intake/expenses))
        employee_count = int(input('how many employees do business have: '))
        print('business earned {} money per employee'.format(intake / employee_count))


def running_calculator():
    initial_result = float(input('enter initial running result: '))
    desired_result = float(input('enter desired result: '))

    calculated_result = initial_result
    day = 1
    while calculated_result <= desired_result:
        calculated_result *= 1.1
        day += 1

    print('runner will achieve desired result on {}-th day'.format(day))


# first_exercise()
# seconds_convert()
# strange_sum()
# max_num_in_string()
# intake_calculator()
# running_calculator()
