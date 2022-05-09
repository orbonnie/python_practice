weight = input('What is your weight in lbs? ')
height = input('What is your height in inches? ')

bmi = (int(weight) * 703) / (int(height) ** 2)

if bmi > 39.9:
  print('The bmi is morbidly obese')
else:
  if bmi > 34.9:
    print('The bmi is severely obese')
  else:
    if bmi > 29.9:
      print('The bmi is moderately obese')
    else:
      if bmi > 24.9:
        print('The bmi is overweight')
      else:
        if bmi > 18.4:
          print('The bmi is normal')
        else:
          if bmi > 15.9:
            print('The bmi is underweight')
          else:
            print('The bmi is severely underweight')