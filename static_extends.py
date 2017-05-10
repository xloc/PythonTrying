class A(object):
    count = 0


class Aa(A):
    def __init__(self):
        Aa.count += 1


class Ab(A):
    def __init__(self):
        Ab.count += 1

if __name__ == '__main__':
    A()
    print A.count

    Aa()
    print A.count, Aa.count
    Aa()
    print A.count, Aa.count

    Ab()
    print A.count, Aa.count, Ab.count
    Ab()
    print A.count, Aa.count, Ab.count

