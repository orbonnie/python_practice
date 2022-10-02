import requests
from random import choice
import pyfiglet
from termcolor import colored

url = "https://icanhazdadjoke.com/search"
header = pyfiglet.figlet_format("DAD JOKES")
header =colored(header, 'yellow', 'on_blue')
print(header)

key = input("What kind of joke do you want to hear? ")

r = requests.get(url,  headers={"Accept": "application/json"}, params={"term": key})

data = r.json()
size = data['total_jokes']

if size == 0:
  print(f"I don't have any jokes about {key}")

else:
  rand = choice(data['results'])

  print(f"I've got {size} jokes about {key}. Here's one:")
  print(rand['joke'])