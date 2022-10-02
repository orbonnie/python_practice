import requests

url = "https://icanhazdadjoke.com/"
search = "https://icanhazdadjoke.com/search"

t = requests.get(url, headers={"Accept": "text/plain"})
j = requests.get(url, headers={"Accept": "application/json"})
s = requests.get(search, headers={"Accept": "text/plain"}, params={"term": "cat", "limit": 2})

data = j.json()

# print(t.text)
# print(data["joke"])

print(s.text)