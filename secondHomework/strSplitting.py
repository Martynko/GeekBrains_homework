def str_splitting():
    user_input = input('please enter some string: ').split()
    i = 1
    for word in user_input:
        print('{} {}'.format(i, word[:10]))
        i += 1


str_splitting()
