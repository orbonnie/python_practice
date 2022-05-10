from random import randint

dice = input('How many dice would you like to roll? ')
sides = input('How many sides should each die have? ')
dice = range(int(dice))
sides = int(sides)

while True:
  results = '|'
  for die in dice:
    roll = randint(1, sides)
    results += f'{roll}|'
  print(results)

  reply = input('Roll again? (q to quit) ')
  if reply == 'q':
    break