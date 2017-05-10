class LearnPropertyDecorator(object):
    def __init__(self):
        self._field = 'hello'

    def __str__(self):
        return '<lpd: %s>' % self._field

    @property
    def field(self):
        print self, 'GET PROPERTY'
        return self._field

    @field.setter
    def field(self, value):
        print self, 'SET PROPERTY'
        self._field = value

if __name__ == '__main__':
    o = LearnPropertyDecorator()
    print o.field
    o.field = 'world'
    print o.field
