import sqlite3
conn = sqlite3.connect('users.db')

c = conn.cursor()

# c.execute('create table users (username text, password text)')

# users = [
#   ('Colt', 'rgd43fre4tfe3gd3w'),
#   ('Leslie', 'fgrtresdr344543'),
#   ('Blue', 'Meow')
# ]

# query = "insert into users values (?, ?)"
# c.executemany(query, users)
u = input('Enter your username ').strip()
p = input('Enter your password ').strip()

# SQL injection
# query = f"select * from users where username='{u}' and password ='{p}'"
query = "select * from users where username=? and password =?"
c.execute(query, (u, p))
result = c.fetchone()

if result:
    print('Welcome Back')
else:
    print('signin failed')


conn.commit()
conn.close()
