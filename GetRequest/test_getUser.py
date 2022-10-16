import requests
import json

url = "https://reqres.in/api/users?page=2"


def test_getResponse():
    response = requests.get(url)
    print(response.url)
    print(response.status_code)
    print(response.headers)
    print(response.cookies)
    assert response.text.__contains__('Lawson') and response.url=="https://reqres.in/api/users?page=2"