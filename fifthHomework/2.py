
def string_counter(file_path):
    with open(file_path, 'r') as file:
        word_counts = []
        line_count = 0
        for line in file:
            word_counts.append(line.split().__len__())
            line_count += 1

        print('file {} contains {} lines with {} words responcively'.format(
            file_path, line_count, word_counts))


string_counter('secondFile.txt')
