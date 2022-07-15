import requests

payload = {"method": "POST"}
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
print(response.text)
print(response.status_code)