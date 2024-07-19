import requests

url = 'http://localhost:5000/process'
input_text = 'Hello, how are you?'
response = requests.post(url, json={'text': input_text})

try:
    response_data = response.json()
    print(response_data)
except requests.exceptions.JSONDecodeError as e:
    print(f"Failed to decode JSON response: {e}")
    print(f"Response text: {response.text}")
