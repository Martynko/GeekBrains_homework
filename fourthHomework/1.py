from sys import argv

work_hours, salaty_per_hour, bonus = argv


def salary_calc(hours, per_hour, bonus):
    print(hours * per_hour + bonus)


salary_calc(work_hours, salaty_per_hour, bonus)
