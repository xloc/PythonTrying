
# $c#87
# $g#8b
# $t10001#8a

d = '\x04'


s = sum([ord(c) for c in d]) & 0xff


print '{:0=2x}'.format(s)
