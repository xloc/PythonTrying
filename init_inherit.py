class Class(object):
    def __init__(self):
        print "init Class"


class SubClass(Class):
    # def __init__(self):
    #     super(SubClass, self).__init__()
    #     print "init SubClass"
    pass


SubClass()
