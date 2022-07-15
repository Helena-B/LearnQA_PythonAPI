import requests

payload = {"method": "HEAD"}
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
print(response.text)
print(response.status_code)