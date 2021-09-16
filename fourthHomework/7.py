
def fact(n):
    for i in range(1, n+1):
        f = 1
        num = 1
        while num <= i:
            f *= num
            num += 1
        yield f


factorials = [el for el in fact(5)]
print(factorials)
