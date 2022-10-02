from pyfiglet import figlet_format as draw
from termcolor import colored

colors = ('red', 'blue', 'green', 'yellow', 'white', 'cyan', 'magenta')
msg = input('Enter your text: ')
color = input('What color would you like? ')
if color not in colors:
    color = 'yellow'
print(colored(draw(msg), color))
