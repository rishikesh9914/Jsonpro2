import requests

url = "https://trains.p.rapidapi.com/"

payload = "{\r\n    \"search\": \"konark\"\r\n}"
headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "187e086a26msh906809c8bca56cep179fe3jsn17f786d19737",
    'x-rapidapi-host': "trains.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)