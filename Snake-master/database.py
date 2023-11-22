import sqlite3

con = sqlite3.connect("Data/data.db", check_same_thread=False)

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS player_scores(player, score)")
con.commit()


# cur.execute("DROP TABLE users")
# con.commit()
cur.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT, score INTEGER DEFAULT 0)")
con.commit()

def add_user(name, password):
    cur.execute(f"INSERT INTO users VALUES('{name}', '{password}', 0)")
    con.commit()
    print("Success")

def show_users():
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    return data

def check_user(name, password):
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    for i in data:
        if i[0] == name and i[1] == password:
            return True
    return False

def add_score(name, score):
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    for i in data:
        if i[0] == name:
            new_score = int(i[2]) + int(score)
            cur.execute(f"UPDATE users SET score = {new_score} WHERE username = '{name}'")
            con.commit()


def show_table():
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    return data