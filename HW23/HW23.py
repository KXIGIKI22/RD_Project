import sqlite3

conn = sqlite3.connect("/Users/pavlo/Documents/Python/book_store.sqlite")
cursor = conn.cursor()

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  age INT
);
"""

create_publishing_house_table = """
CREATE TABLE IF NOT EXISTS publishing_house (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  rating INT DEFAULT 5
);
"""

create_books_table = """
CREATE TABLE IF NOT EXISTS books (
  id INT PRIMARY KEY,
  title VARCHAR(255),
  author VARCHAR(255),
  year INT,
  price DECIMAL(10, 2),
  publishing_house_id INT,
  FOREIGN KEY (publishing_house_id) REFERENCES publishing_house(id)
);
"""

create_purchases_table = """
CREATE TABLE IF NOT EXISTS purchases (
  id INT PRIMARY KEY,
  user_id INT,
  book_id INT,
  date DATE,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (book_id) REFERENCES books(id)
);
"""


cursor.execute(create_users_table)
cursor.execute(create_publishing_house_table)
cursor.execute(create_books_table)
cursor.execute(create_purchases_table)


conn.commit()
conn.close()