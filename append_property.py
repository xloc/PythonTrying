class HasListProperty(object):
    def __init__(self):
        self._arr = []
        # self._arr = 3

    @property
    def arr(self):
        print 'get arr'
        return self._arr

    @arr.setter
    def arr(self, value):
        print "set arr"
        self._arr = value

if __name__ == '__main__':
    a = HasListProperty()

    a.arr.append('a')
    a.arr.append('b')

    # a.arr += 1
    # a.arr += 5

    print a.arr
