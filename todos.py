
from urllib import response


header = '''
 _____         _
|_   _|__   __| | ___  ___
  | |/ _ \ / _` |/ _ \/ __|
  | | (_) | (_| | (_) \__
  |_|\___/ \__,_|\___/|___/'''

help = '''
TODO LIST HELP
Type 'q' to quit
To add a todo to the list, type it and hit enter
To complete a todo enter its number
'''
# quit = input()
todos = []
completed = []

def get_input():
  print('***********************************')
  task = input("Enter a command. Type 'h' for help: " )
  route_cmd(task)

def route_cmd(cmd):
  if cmd == 'h':
    show_help()
  elif cmd.isnumeric():
    remove_task(int(cmd))
  elif cmd:
    add_task(cmd)

def add_task(task):
  todos.append(task)
  show_tasks()

def remove_task(num):
  if num <= len(todos) and num > 0:
    done = todos.pop(num - 1)
    completed.append(done)
  else:
    print(f'There is no task at number {num}')
  show_tasks()

def show_help():
  response = input(help)
  route_cmd(response)

def show_tasks():
  for index in range(len(todos)):
    print(f'{index + 1}) {todos[index]}')

def end_tasks():
  print(f'Today you completed {len(completed)} todos: ')
  for t in completed:
    print(f'* {t}')

print(header)
while True:
  print('***********************************')
  task = input("Enter a command. Type 'h' for help: " )
  if task == 'q':
    end_tasks()
    break
  route_cmd(task)
