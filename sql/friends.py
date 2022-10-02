import sqlite3
conn = sqlite3.connect('my_friends.db')

#create cursor
c = conn.cursor()
#execute sql with cursor
#c.execute("create table friends (first_name text, last_name text, closeness integer);")
#insert_query = "insert into friends values ('Mary', 'Lee', 4);"

# data = [
#   ('Nate', 'Larry', 6),
#   ('Chris', 'Kay', 3),
#   ('Wilma', 'Wilks', 7),
#   ('Scott', 'Smith', 1)
# ]

#query = "insert into friends values (?, ?, ?)"
# for p in data:
#     c.execute(query, p)

# or c.executemany(query, data)

query = "select * from friends order by closeness desc"
c.execute(query)
# print(c.fetchall())
print(c.fetchone())
# for result in c:
#   print(result)

conn.commit()
conn.close()