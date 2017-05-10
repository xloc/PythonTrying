
uid_map = {}
isbn_map = {}

with open('./input.csv') as f:
    f.readline()
    for ln in f.xreadlines():
        uid, isbn, rating = ln[:-1].split(';')
        if uid not in uid_map:
            uid_map[uid] = len(uid_map)
        if isbn not in isbn_map:
            isbn_map[isbn] = len(isbn_map)


umf = open('./uid-map', 'w')
for k, v in uid_map.iteritems():
    umf.write('{};{}\n'.format(k, v))
umf.close()

imf = open('./isbn-map', 'w')
for k, v in isbn_map.iteritems():
    imf.write('{};{}\n'.format(k, v))
imf.close()


irdf = open('./isbn-rearranged-data', 'w')
with open('./input.csv') as f:
    f.readline()
    for ln in f.xreadlines():
        uid, isbn, rating = ln[:-1].split(';')
        irdf.write('{};{};{}\n'.format(
            uid_map[uid], isbn_map[isbn], rating
        ))
irdf.close()
