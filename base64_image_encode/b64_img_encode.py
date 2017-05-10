import base64
import glob
import json
from sys import argv

if __name__ == '__main__':
    if len(argv) == 1:
        path = './imgs/*'
    elif len(argv) == 2:
        path = argv[1]
    else:
        raise Exception('Wrong argument')

    imgs = {}

    for p in glob.glob(path):
        name = p.rsplit('/', 1)[1]
        print '{} -> {}'.format(p, name)
        with open(p) as img:
            imgs[name] = base64.b64encode(img.read())


    f = open('b64_imgs.json', 'w')
    json.dump(imgs, f)
    f.close()
