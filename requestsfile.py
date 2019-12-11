import requests
from requests.adapters import HTTPAdapter
import json


#send request
#Post request to a login url
try:
    data = {
        "username" : "myusername",
        "password" : "mypassword"
    }
    print(123)
    response = requests.post('http://127.0.0.1:8000/customusers/login/', data=data)
    if response.status_code == 200:
        body = response.json()
        token = body['token']
        print("succesful")
    else:
        print("Unsuccesful request: Code: ", response.status_code)
        print("Details: ", response.content)
except requests.exceptions.RequestException as e:
    print("Error ot type ",type(e).__name__, " occured with details: ", str(e))


#get request (with headers)
try:
    headers = {
        'Authorization' : 'Token '+token
    }
    response = requests.get('http://127.0.0.1:8000/customusers/', headers=headers)
    if response.status_code == 200:
        body = response.json()
        # print(body) uncomment to view body
        print("succesful")
    else:
        print("Unsuccesful request: Code: ", response.status_code)
        print("Details: ", response.content)
except requests.exceptions.RequestException as e:
    print("Error ot type ",type(e).__name__, " occured with details: ", str(e))

#get request with parameters
try:
    headers = {'Authorization' : 'Token '+token}
    payload = {'usertype': 'AGENT'}

    response = requests.get('http://127.0.0.1:8000/customusers/getusersofsertype/', headers=headers, params=payload)
    if response.status_code == 200:
        body = response.json()
        # print(body) uncomment to view body
        print("succesful")
    else:
        print("Unsuccesful request: Code: ", response.status_code)
        print("Details: ", response.content)
except requests.exceptions.RequestException as e:
    print("Error of type ",type(e).__name__, " occured with details: ", str(e))

#extract an image from API response
try:
    headers = {'Authorization' : 'Token '+token}
    payload = {'usertype': 'AGENT'}

    response = requests.get('http://127.0.0.1:8000/agents/5/getavatar/', headers=headers, params=payload)
    if response.status_code == 200:
        body = response.content
        with open('file', 'wb') as writer:
            writer.write(body)
        print("succesful")
    else:
        print("Unsuccesful request: Code: ", response.status_code)
        print("Details: ", response.content)
except requests.exceptions.RequestException as e:
    print("Error ot type ",type(e).__name__, " occured with details: ", str(e))

#post a multipart data (with timeout)
try:
    headers = {'Authorization' : 'Token '+token}
    data = {"agentNationalID" : 33255192}
    
    with open('profile.jpeg', 'rb') as myfile:
        files = {
            "agentAvatar" : myfile
        }
        response = requests.post('http://127.0.0.1:8000/agents/updateavatar/', data=data, files=files, headers=headers, timeout=60)
    
    if response.status_code == 200:
        # print(response.content)
        print("succesful")
    else:
        print("Unsuccesful request: Code: ", response.status_code)
        print("Details: ", response.content)
except requests.exceptions.RequestException as e:
    print("Error ot type ",type(e).__name__, " occured with details: ", str(e))



#a transport adpater for retries
github_adapter = HTTPAdapter(max_retries=5)

session = requests.Session()

# Use `github_adapter` for all requests to endpoints that start with this URL
session.mount('https://api.github.com', github_adapter)

try:
    session.get('https://api.github.com')
except requests.exceptions.RequestException as e:
    print("Error ot type ",type(e).__name__, " occured with details: ", str(e))
