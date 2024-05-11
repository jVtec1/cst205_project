import requests, json
models = ["rx-7", "gt-r", "240sx", "supra", "s2000", "rsx", "300zx", "nsx", "integra", "350z", "prelude", "lancer evo", "impreza", "miata", "civic", "mr2"]
info_bank = []

for i in range(len(models)):
    api_url_test = 'https://api.api-ninjas.com/v1/cars?limit=2&model={}'.format(models[i])
    response_test = requests.get(api_url_test, headers={'X-Api-Key': 'vuO4AjxkNC05YF/LQBTSxQ==SBzevRW7eeax5zZY'})
    if response_test.status_code == requests.codes.ok:
        text = response_test.json()
        info_bank.append(text[0])
    else:
        print("Error:", response_test.status_code, response_test.text)
