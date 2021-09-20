def lessons_sum(file_path):
    dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            s = line.replace('(', ' ').split()
            sum = 0
            for part in s:
                if part.isnumeric():
                    sum += int(part)
            dict[s[0]] = sum
    print(dict)


lessons_sum('sixthFile.txt')
