import sqlite3

conn = sqlite3.connect("/Users/pavlo/Documents/database_1.sqlite")
cursor = conn.cursor()

# Запит 1: Вибір усіх записів із таблиці users старше 30 років
query1 = "SELECT * FROM users WHERE age > 30;"
cursor.execute(query1)
result1 = cursor.fetchall()
print("Результат запиту 1:")
for row in result1:
    print(row)

# Запит 2: Виведення кількості записів в таблиці users, що старше 30 років
query2 = "SELECT COUNT(*) FROM users WHERE age > 30;"
cursor.execute(query2)
result2 = cursor.fetchone()
print("Результат запиту 2:")
print("Кількість записів:", result2[0])

# Запит 3: Виведення інформації про вік та кількість користувачів
query3 = "SELECT age, COUNT(*) AS users FROM users GROUP BY age;"
cursor.execute(query3)
result3 = cursor.fetchall()
print("Результат запиту 3:")
for row in result3:
    print(row[0], "|", row[1])

# Запит 4: Виведення даних відсортованих за кількістю користувачів у спадаючому порядку та по віку у зростаючому порядку
query4 = "SELECT age, COUNT(*) AS users FROM users GROUP BY age ORDER BY users DESC, age ASC;"
cursor.execute(query4)
result4 = cursor.fetchall()
print("Результат запиту 4:")
for row in result4:
    print(row[0], "|", row[1])

# Запит 5: Модифікація запиту 4 для вибору записів з значенням users більше 1
query5 = "SELECT age, users FROM (SELECT age, COUNT(*) AS users FROM users GROUP BY age) AS subquery WHERE users > 1;"
cursor.execute(query5)
result5 = cursor.fetchall()
print("Результат  запиту 5:")
for row in result5:
    print(row[0], "|", row[1])

conn.close()