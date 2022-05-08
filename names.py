first = input('What is your first name? ')
last = input('What is your last name? ')
first = first.strip()
last = last.strip()
length = len(first) + len(last)

if length == 12:
  print(f'{first} {last} is exactly as long as the average name')

elif length > 12:
  print(f'{first} {last} name is longer than the average name')

else :
  print(f'{first} {last} is shorter than the average name')

print('*' * 45)