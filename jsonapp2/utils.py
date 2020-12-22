import requests
def search_train(train_name):
    url = "https://trains.p.rapidapi.com/"

    payload = "{\r\"search\": \""+train_name+"\"\r}"

    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "187e086a26msh906809c8bca56cep179fe3jsn17f786d19737",
        'x-rapidapi-host': "trains.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text