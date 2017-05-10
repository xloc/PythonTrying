class U(object):

    a = 10086

    def __init__(self):
        self.b = U.a


class B(object):
    def __init__(self):
        self.access = a