from termcolor import colored

text = colored('Hi There!', 'red', 'on_white', attrs=['blink'])
print(text)