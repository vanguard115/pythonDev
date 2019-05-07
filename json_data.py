
import json

data = '''
[
    {
      "id" : "001",
       "x" : "2",
       "name" : "Chuck"
     } ,

     {
       "id" : "009",
        "x" : "7",
        "name" : "Brent"
     }
]'''


info = json.loads(data)

print('# DEBUG: ',info)
print('User Count: ',len(info))

for item in info:
    print('# DEBUG: ',item,type(item))
    # print('Name',item['name'])
    # print('Id', item['id'])
    # print('Attribute', item['x'])
