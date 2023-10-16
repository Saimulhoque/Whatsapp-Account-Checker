
import requests

url = "https://api.p.2chat.io/open/whatsapp/check-number/<your-number>/<number-to-check>"

payload={}
headers = {
  'X-User-API-Key': ''
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

