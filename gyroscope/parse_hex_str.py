i = raw_input()
hs = i.split()

hs = map(lambda s: int(s, base=16), hs)


ss = sum(hs) & 0xff
print hex(ss)