import csv
import json
import requests

url = 'https://rest.iad-06.braze.com/users/track'
API_KEY = 'Bearer api_key'
headers = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
}

with open('batch_test_2.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for row in spamreader:
        if len(row)==0:
            continue
        temp = row[0].split(",")
        # print(temp)
        dic = {}
        if temp[0] == "external_id":
            continue
        if temp[0] != "":
            dic["external_id"] = temp[0]
        if temp[1] != "":
            dic["bool_test"] = bool(temp[1])
        if temp[2] != "":
            dic["offer_codes_used"] = temp[2]
        if temp[3] != "":
            dic["num_test"] = int(temp[3])
        if temp[4] != "":
            dic["time_test"] = temp[4]
        if temp[5] != "":
            dic["array_test"] = temp[5].split("|")

        body = json.dumps({"attributes" : [dic]})
        response = requests.post(url, data=body, headers=headers)
        print(response.json())
