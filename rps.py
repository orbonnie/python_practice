from random import choice

rock = """
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

plays = [rock, paper, scissors]
player = input('Choose rock(r), paper(p), or scissiors(s) ')
player = player.lower()
if player == 'r':
  player = rock
elif player == 'p':
  player = paper
elif player == 's':
  player = scissors
else:
  player = ''
  player = input('Please choose r, p, or s')
  if player == 'r':
    player = rock
  elif player == 'p':
    player = paper
  elif player == 's':
    player = scissors

computer = choice(plays)
print(f'YOUR MOVE: {player}')
print(f'Computer chooses {computer}')

if player == computer:
  print('Its a tie! Try again.')

if player == rock and computer == paper:
  print('Computer wins')
elif player == rock and computer == scissors:
  print('Player1 wins')

if player == paper and computer == scissors:
  print('Computer wins')
elif player == paper and computer == rock:
  print('Player1 wins')

if player == scissors and computer == rock:
  print('Computer wins')
elif player == scissors and computer == paper:
  print('Player1 wins')