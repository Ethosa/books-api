from sqlite3 import connect, Cursor, Connection

db: Connection = connect('test.db')
cur: Cursor = db.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS user (
    id integer PRIMARY KEY AUTOINCREMENT,
    login varchar(24),
    password varchar(64)
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS books (
    id integer PRIMARY KEY AUTOINCREMENT,
    title varchar(64),
    description varchar(512),
    image_link varchar(128)
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS favorite (
    id integer PRIMARY KEY AUTOINCREMENT,
    user_id integer,
    book_id integer
);
''')
db.commit()
