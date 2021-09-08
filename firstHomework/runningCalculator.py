def running_calculator():
    initial_result = float(input('enter initial running result: '))
    desired_result = float(input('enter desired result: '))

    calculated_result = initial_result
    day = 1
    while calculated_result <= desired_result:
        calculated_result *= 1.1
        day += 1

    print('runner will achieve desired result on {}-th day'.format(day))


running_calculator()
