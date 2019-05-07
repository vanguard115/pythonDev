import xml.etree.ElementTree as ET

data = '''
<person>
    <users>
    <user x='1'>
        <name>Chuck</name>
        <phone type="intl">
        +1 734 303 4456
        </phone>
        <email hide="yes" />
    </user>
    <user x='2'>
        <name>Ruben</name>
            <phone type="intl">
            +1 9744706991
            </phone>
            <email hide="no" />
        </user>
    </users>
</person>'''

tree = ET.fromstring(data)
# print('# DEBUG: ',tree)
# print('Name:', tree.find('name').text)
# print('Phone:', tree.find('phone').text.strip())
# print('Phone type' , tree.find('phone').get('type'))
# print('Attr:', tree.find('email').get('hide'))

people = tree.findall('user')
people2 = tree.findall('users/user')
print('# DEBUG: ',len(people))
print('# DEBUG: ',len(people2))

for dude in people2:
    print('Name: ',dude.find('name').text)
    print('Phone Num: ',dude.find('phone').text)
    print('Email hide: ',dude.find('email').get('hide'))
    print('Attribute: ',dude.get('x'))
