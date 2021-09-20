translation = {
    'One': 'один',
    'Two': 'два',
    'Three': 'три',
    'Four': 'четыре'
}


def translator(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        new_file_content = []
        for line in file:
            l = line.split()
            l[0] = (translation[l[0]])
            translated = ''.join(l)
            new_file_content.append(translated)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for line in new_file_content:
            file.write(line + '\n')
        file.flush()


translator('fourthInput.txt', 'fourthOutput.txt')
