player1 = input('enter player one\'s name ')
player2 = input('enter player two\'s name ')
toothpicks = 13
turn = player1

while toothpicks > 0:
  holder = ''
  for x in range(toothpicks):
    holder += '| '
  print(holder)
  print(f'There are {toothpicks} toothpicks left')
  choice = int(input(f'How many will you take, {turn}? '))

  while choice > 3 or choice < 1:
    choice = int(input('You can only take 1, 2, or 3: '))

  while choice > toothpicks:
    print(f'There are only {toothpicks} toothpicks left.')
    choice = int(input('How many would you like? '))
  print(choice)

  toothpicks -= choice
  if toothpicks == 0:
    print(f'{turn} wins!')
    break

  if turn == player1:
    turn = player2
  else:
    turn = player1