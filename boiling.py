unit = input('What temperature unit are you using? ')
temp = input('What temperature is the water? ')
temp = int(temp)

if unit == 'f':
  if temp >= 212:
    print('The water is boiling')
  else:
    print('The water is not boiling')

if unit == 'c':
  if temp >= 100:
    print('The water is boiling')
  else:
    print('The water is not boiling')

if unit == 'k':
  if temp >= 373:
    print('The water is boiling')
  else:
    print('The water is not boiling')
