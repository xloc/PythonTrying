import injectee


def fun(**kwargs):
    for k, w in kwargs.iteritems():
        setattr(injectee, k, w)
injectee.fun = fun
