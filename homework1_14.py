import sqlite3

# Код из предыдущего задания

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

#
# balance = 1000
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)", (f'User{i}',
#                                                                                           f'example{i}@gmail.com',
#                                                                                           f'{i*10}', f'{balance}'))
#
# cursor.execute('UPDATE Users SET balance = ? WHERE id % 2!=0', (500, ))
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE id = ?', (i, ))

# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60, ))
# users = cursor.fetchall()
# for user in users:
#     print(user)

# Удаление пользователя с id=6
# cursor.execute('DELETE FROM Users WHERE id = ?', (6, ))

# Подсчёт кол-ва всех пользователей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
# print(total_users)

# Подсчёт суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
# print(all_balances)
print(all_balances / total_users)


connection.commit()
connection.close()
