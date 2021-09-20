import json


def profit_calc(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        companies = [get_company_data(l) for l in file]
        sum = 0
        count = 0
        for c in companies:
            if c[1] > 0:
                sum += c[1]
                count += 1

    print('average profit {}, companies counted {}'.format(sum/count, count))
    return sum/count


def json_convert(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        companies = [get_company_data(l) for l in file]
        dict = {c[0]: c[1] for c in companies}
        dict['average_profit'] = profit_calc(file_path)

    with open("seventhOutput.json", "w") as write_f:
        json.dump(dict, write_f)


def get_company_data(str):
    s = str.split()
    profit = int(s[2]) - int(s[3])
    return (s[0], profit)


# profit_calc('seventhFile.txt')
json_convert('seventhFile.txt')
