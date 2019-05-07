import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '20'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()


    js = json.loads(data)
    print('# DEBUG: ',type(js))
    print(json.dumps(js, indent=2))
    # headers = dict(connection.getheaders())
    # print headers
    # print('Remaining', headers['x-rate-limit-remaining'])

    print('# DEBUG: ','Out of loop')
    # print(js['users'])
    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print(' * No status found')
            continue
        s = u['status']['text']
        print(' ', s[:50])
