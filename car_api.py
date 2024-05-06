import requests, json
from urllib.request import urlopen

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