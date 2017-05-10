def y():
    for i in range(10):
        print i,
        yield i


for i in y():
    if i >= 5:
        break