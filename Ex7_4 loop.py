import requests

payload = {"method1": "GET", "method2": "POST", "method3": "PUT", "method4": "DELETE"}

for value in payload.values():
    if value == "GET":
        for item in payload.items():
            response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=value)
            print(value)
            print(response.text)
            print(response.status_code)


    if value == "POST":
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=value)
        print(value)
        print(response.text)
        print(response.status_code)
    if value == "PUT":
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=value)
        print(value)
        print(response.text)
        print(response.status_code)
    if value == "DELETE":
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=value)
        print(value)
        print(response.text)
        print(response.status_code)