import urllib,urllib2
import sys
import json
import os
import base64
reload(sys)
sys.setdefaultencoding('utf-8')


def recognize(filepath, ftype, frate, token, fchannel):

    fh = open(filepath,'rb')
    content = fh.read()

    f_len = os.path.getsize(filepath)
    speech = base64.b64encode(content)

    fh.close()

    cuid = "00-36-76-26-06-24"
    url = 'http://vop.baidu.com/server_api'

    update = json.dumps({'format':ftype,'rate':frate,'channel':fchannel,'cuid':cuid,'token':token,'speech':speech,'len':f_len})

    r = urllib2.urlopen(url, update)

    result = json.loads(r.read())

    print(result)

    text = result['result'][0]

    return text

if __name__=='__main__':
    Api_Key = 'mWiZlsymBq3B6OGyuaE3W2EE'
    Secrect_Key = '60ff9ec6be5711e48b492f9bf8b4ae6d'
    path= 'iflytek01.wav'
    url1 = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + Api_Key + '&client_secret=' + Secrect_Key
    res = urllib2.urlopen(url1).read()
    data = json.loads(res)
    token = data['access_token']
    results=recognize(path, 'wav', 16000, token, 1)
    print results