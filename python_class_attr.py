class Demo:
    a = 0

    @classmethod
    def print_a(cls):
        print cls.a

    def acc_a(self):
        Demo.a += 1


d1 = Demo()
d1.acc_a()
Demo.print_a()

d2 = Demo()
d2.acc_a()
Demo.print_a()

