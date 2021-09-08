def seconds_convert():
    seconds = float(input('input seconds: '))
    print('{:02}:{:02}:{:02}'.format(int(seconds // 3600),
          int(seconds % 3600//60), int(seconds % 60)))


seconds_convert()
