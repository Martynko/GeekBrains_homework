def intake_calculator():
    intake = float(input('please enter business intake: '))
    expenses = float(input('please enter business expenses: '))

    if intake <= expenses:
        print('business earned no profit')
    else:
        print('profitability of proceeds {}'.format(
            (intake - expenses)/expenses))
        employee_count = int(input('how many employees do business have: '))
        print('business earned {} money per employee'.format(
            intake / employee_count))


intake_calculator()
