import sqlite3

connection = sqlite3.connect('schedule.db')

cur = connection.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (telegram_id  BIGINT, group_number TEXT)')
connection.commit()
cur.close()


def register_user(telegram_id):
    cur = connection.cursor()
    cur.execute('SELECT * FROM users WHERE telegram_id = ?', (telegram_id,))
    data = cur.fetchall()
    if len(data) != 0:
        cur.close()
        return 'false'
    cur.execute('INSERT INTO users (telegram_id, group_number) VALUES (?, ?)', (telegram_id, 'no group number'))
    connection.commit()
    cur.close()
    return 'true'


def add_fav_group(telegram_id, group_number):
    cur = connection.cursor()
    cur.execute('UPDATE users SET group_number = ? WHERE telegram_id = ?', (group_number, telegram_id))
    connection.commit()
    cur.close()


def check_group_number_set(telegram_id):
    cur = connection.cursor()
    cur.execute('SELECT group_number FROM users WHERE telegram_id = ?', (telegram_id,))
    data = cur.fetchone()
    cur.close()
    return not data[0] == 'no group number'


def get_group_number(telegram_id):
    cur = connection.cursor()
    cur.execute('SELECT group_number FROM users WHERE telegram_id = ?', (telegram_id,))
    data = cur.fetchone()
    cur.close()
    return data[0]


def get_all_users():
    cur = connection.cursor()
    cur.execute('SELECT * FROM users')
    data = cur.fetchall()
    cur.close()
    return data
