import urllib.request
import urllib.parse
import json

serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'sensor': 'false', 'address': address})
    print('Retrieving',url)

    uh = urllib.request.urlopen(url)
    print('Type of uh is:',type(uh))
    data = uh.read()
    # data = str(data)
    # print('Type of data is:', type(data))
    print('Retrieved',len(data),'characters')

    try:
        info = json.loads(data.decode("utf-8"))
    except:
        info = None

    print('Type of info is:',type(info))

    if "status" not in info or info["status"] != "OK":
        print('========= Failure to Retrieve =========')
        print(data)
        continue

    print(json.dumps(info, indent=4)) #json parse the dictionary "info" and is
    # using pretty printing with identation of 4

    lat = info["results"][0]["geometry"]["location"]["lat"]
    lng = info["results"][0]["geometry"]["location"]["lng"]
    print('lat:',lat,'\nlng:',lng)

    location = info["results"][0]["formatted_address"]
    print(location)