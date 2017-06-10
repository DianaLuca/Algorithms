import json

data = '''{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
    },
    "email": {
        "hide": "yes"
    }

}'''

print('type of data:',type(data))

info = json.loads(data)

print('type of info (json.loads(data)):',type(info))

print('Name', info['name'])
print('Hide', info['email']['hide'])
