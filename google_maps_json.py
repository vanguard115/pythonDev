import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = True
# If you have a Google Places API key, enter it here
api_key = 'AIzaSyAoslx58HMdHnr8hQwQN84SmZL_rhsNGfA'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    try:
        lat = js['results'][0]['geometry']['location']['lat']
        lng = js['results'][0]['geometry']['location']['lng']
        print('lat', lat, 'lng', lng)
        print('Country code :',js['results'][0]['address_components'][3]['short_name'])
    except:
        try:
            if js['results'][0]['address_components'][0]['types'][1]:
                print('Country code does not exist, this is a',js['results'][0]['address_components'][0]['types'][1])
        except:
            print('This is something else, likr the pole or somethign')

    location = js['results'][0]['formatted_address']
    print(location)
