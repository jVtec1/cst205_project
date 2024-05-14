# Anthony Constante, Andy Espinoza, Abel Plascencia, Emily Grimaldo
# CST205
# This file was initiated and completed by Andy Espinoza
import requests, json
from urllib.request import urlopen

#shorter list to test loop
models = ["camry", "accord", "civic"]
#bigger list that we will actually use that has all the car models we want(subject to change)
'''
models = ["camry", "accord", "civic", "supra", "mustang", "charger", "challenger", "nsx", "integra", "350z"]
'''
#the varible that will be imported and used
info_bank = []

#previous commit information (lines 13-31)
'''
#the variable we are passing in is a car model and will get all of its information 
model = 'camry'
#code to get the information from the api
api_url = 'https://api.api-ninjas.com/v1/cars?limit=2&model={}'.format(model)
response = requests.get(api_url, headers={'X-Api-Key': 'vuO4AjxkNC05YF/LQBTSxQ==SBzevRW7eeax5zZY'})

#successful request to the api
if response.status_code == requests.codes.ok:
    text = response.json()
    #getting specific iformation 
    print(text[0]['transmission'])
    #returns all information from the request as a list/dictionary
    #print(response.text)
#unsuccessful 
else:
    print("Error:", response.status_code, response.text)
'''


#looping through list to get info from api and deposit in a varible to easily all info needed from one varible
for i in range(len(models)):
    api_url_test = 'https://api.api-ninjas.com/v1/cars?limit=2&model={}'.format(models[i])
    response_test = requests.get(api_url_test, headers={'X-Api-Key': 'vuO4AjxkNC05YF/LQBTSxQ==SBzevRW7eeax5zZY'})
    if response_test.status_code == requests.codes.ok:
        text = response_test.json()
        info_bank.append(text[0])
    else:
        print("Error:", response_test.status_code, response_test.text)

#prints all information stored in variable
#print(info_bank)
#prints all information of the model in index list 0 of "models" list (which is camry in this case)
print(info_bank[0])
#prints specific information of that model, in this case the year. 
#print(info_bank[0]['year'])