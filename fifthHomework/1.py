

def save_file(str_lst):
    with open('firstFile.txt', 'w') as file:
        for str in str_lst:
            file.write(str + '\n')


def read_lines():
    str_lst = []
    str = input('input some text (enter emty text to save): \n')
    while str != '':
        str_lst.append(str)
        str = input('')
    return str_lst


save_file(read_lines())
