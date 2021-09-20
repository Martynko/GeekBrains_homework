def salary_counter(file_path):
    with open(file_path, 'r') as file:
        les_than_20 = []
        sum = 0
        count = 0
        for line in file:
            s = line.split()
            sum += int(s[1])
            count += 1
            if int(s[1]) < 20000:
                les_than_20.append(s[0])

        print('poor employees are {}'.format(les_than_20))
        print('average salary {}'.format(sum / count))


salary_counter('thirdFile.txt')
