import injector
import injectee

for i in dir(injectee):
    print i, getattr(injectee, i)

injectee.fun(a='not 1', b='not hello', c='not float')

for i in dir(injectee):
    print i, getattr(injectee, i)
