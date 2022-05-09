from random import randint

die1 = randint(1, 6)
die2 = randint(1, 6)

while die1 != 1 and die2 != 1:
  die1 = randint(1, 6)
  die2 = randint(1, 6)
  print(f'you rolled {die1} and {die2}')

print('You rolled snake eyes')


