import requests
import json
import csv
import os
import datetime

# init vars
# check open file
# Query db
# filter the response (its lots of dictionaries in dictionaries then lists and whatever else. Debug each step processing the layers)
# while loop for queries. anything over 2000 ish causes a problem with the module imported
# cancel while loop when the number of queried obituaries is less than the limit on request
# export data to basic csv file

limit = 1000
offset = 0
target = None
response = None
data= None
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

file_name = 'new_obituary_names.csv'
if os.path.exists(file_name):
    os.remove(file_name)

now =datetime.datetime.now()
yesterYear = now - datetime.timedelta(days=365)

obituaries = None
name = None
full_name = None
all_names = []
flag = True

with open('new_obituary_names.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["full name"])  
           

    while flag:

        target = f'https://obits.postandcourier.com/api/_frontend/obituaries?endDate={now.strftime("%Y-%m-%d")}&limit={limit}&noticeType=all&offset={offset}&sortBy=date&startDate={yesterYear.strftime("%Y-%m-%d")}&affiliateSiteName=charleston'
        response = requests.get(target, headers=headers)
        data = json.loads(response.text)

        obituaries = data['obituaries']

        for x in obituaries:
            name = x["name"]
            full_name = f"{name.get('firstName', '')} {name.get('middleName', '')} {name.get('lastName', '')}".strip()
            all_names.append([full_name])
            print(full_name)

        

        if len(obituaries) < limit:
            flag=False
        offset += limit

    writer.writerows(all_names) 



print('The end')

