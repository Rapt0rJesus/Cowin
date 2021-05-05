import requests
import json

'''
Edit State ID
'''
StateID=21




url = f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{StateID}"
payload={}
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


response = requests.request("GET", url, headers=headers, data=payload)
if response.status_code==200:
    for i in response.json()["districts"]:
        print(i["district_name"],"\t\t\t",i["district_id"])
else:
    print("Cowin is presenting cloudflare error, please run the file again or try again after some time")
