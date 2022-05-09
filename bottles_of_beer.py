bottles = range(99, 0, -1)

for bottle in bottles:
  plural2 = 'bottles'
  if bottle == 1:
    plural = 'bottle'
  elif bottle == 2:
    plural2 = 'bottle'
  else:
    plural = 'bottles'

  print(f'{bottle} {plural} of beer on the wall')
  print(f'{bottle} {plural} of beer')
  print(f'Take one down, pass it around, {bottle - 1} {plural2} of beer')