import time
import logging

import psycopg2

conn = psycopg2.connect(
    host="db",
    database="database",
    user="username",
    password="secret",
    port="5432",
)

print('Start demo\n')


# insert 1million rows
# cur = conn.cursor()

# s = time.time()
# for i in range(1000000):
#     print(f'insert row no. {i}\n')
#     timestamp = str(int(round(time.time() * 1000)))
#     cur.execute(
#         "insert into messages (id, timestamp, message) values(%s,%s, %s);",
#         (
#             i,
#             timestamp,
#             f"This is entry with id {i} created on {timestamp}",
#         ),
#     )


# e = (time.time() - s)*1000
# print(f"Insert 1 million rows in {e}ms\n")

# # commit
# conn.commit()



#server side cursor
s = time.time()
cur = conn.cursor("servercursor") # to be a server side cursor, the cursor must be named
e = (time.time() - s)*1000
print(f"Cursor established in {e}ms\n")

s = time.time()
cur.execute("select * from messages")
e = (time.time() - s)*1000
print(f"execute query {e}ms\n")

s = time.time()
rows = cur.fetchmany(50)
e = (time.time() - s)*1000
print(f"fetching first 50 rows {e}ms\n")

cur.close()


#client side cursor
s = time.time()
cur = conn.cursor()
e = (time.time() - s)*1000
print(f"Cursor established in {e}ms\n")

s = time.time()
cur.execute("select * from messages")
e = (time.time() - s)*1000
print(f"execute query {e}ms\n")

s = time.time()
rows = cur.fetchmany(50)
e = (time.time() - s)*1000
print(f"fetching first 50 rows {e}ms\n")

cur.close()


# commit
conn.commit()

# close
conn.close()