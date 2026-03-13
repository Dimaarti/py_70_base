# 1
import sqlite3
from dataclasses import dataclass

conn = sqlite3.connect('library.db')
cursor = conn.cursor()


# cursor.execute('''CREATE TABLE books
#     (id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT,
#     author TEXT,
#     year INTEGER,
#     status TEXT CHECK(status IN ('available''borrowed')) DEFAULT 'available')
# ''')
# cursor.execute('''CREATE TABLE readers (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER)
# ''')
# cursor.execute('''CREATE TABLE borrowed_books (
#     reader_id INTEGER,
#     book_id INTEGER,
#     borrow_date TEXT,
#     FOREIGN KEY (reader_id) REFERENCES readers (id),
#     FOREIGN KEY (book_id) REFERENCES books (id))
# ''')
# conn.commit()

# 2
@dataclass
class Books:
    id: int
    title: str
    author: str
    year: int
    status: str


@dataclass
class Reader:
    id: int
    name: str
    age: int


# 3
class Library:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # self.cursor.execute('''CREATE TABLE books
        #      (id INTEGER PRIMARY KEY AUTOINCREMENT,
        #      title TEXT,
        #      author TEXT,
        #      year INTEGER,
        #      status TEXT DEFAULT 'available')
        # ''')
        # self.cursor.execute('''CREATE TABLE readers (
        #     id INTEGER PRIMARY KEY,
        #     name TEXT,
        #     age INTEGER)
        # ''')
        # self.cursor.execute('''CREATE TABLE borrowed_books (
        #     reader_id INTEGER,
        #     book_id INTEGER,
        #     borrow_date TEXT,
        #     FOREIGN KEY (reader_id) REFERENCES readers (id),
        #     FOREIGN KEY (book_id) REFERENCES books (id))
        # ''')
        pass

    def add_book(self, title, author, year):
        self.cursor.execute(
            "INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
        self.conn.commit()

    def add_reader(self, name, age):
        self.cursor.execute("INSERT INTO readers (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()

    def borrow_book(self, reader_id, book_id):
        self.cursor.execute("SELECT status FROM books WHERE id = ?", (book_id,))
        result = self.cursor.fetchone()
        if result and result[0] == 'available':
            self.cursor.execute("INSERT INTO borrowed_books (reader_id, book_id) VALUES (?, ?)", (reader_id, book_id))
            self.cursor.execute("UPDATE books SET status = 'borrowed' WHERE id = ?", (book_id,))
            self.conn.commit()

    def return_book(self, book_id):
        self.cursor.execute("DELETE FROM borrowed_books WHERE book_id = ?", (book_id,))
        self.cursor.execute("UPDATE books SET status = 'available' WHERE id = ?", (book_id,))
        self.conn.commit()

    def search_books(self, keyword):
        query = "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?"
        self.cursor.execute(query, (f'%{keyword}%', f'%{keyword}%'))
        books = self.cursor.fetchone()
        return books


    def get_borrowed_books(self):
        query = """SELECT readers.name, books.title
        FROM borrowed_books
        JOIN readers ON borrowed_books.reader_id = readers.id
        JOIN books ON borrowed_books.book_id = books.id"""
        self.cursor.execute(query)
        return self.cursor.fetchall()



    def get_statistics(self):
        self.cursor.execute("SELECT status, COUNT(*) FROM books GROUP BY status")
        stats = dict(self.cursor.fetchall())
        return stats




library = Library()
# library.add_book("Great Gatsby", 'Fitzgerald', 1925)
# library.add_reader('Freddy', 26)
# library.borrow_book(2, 3)
# library.return_book(1)
# print(library.search_books('Fitzgerald', ))
# print(library.get_borrowed_books())
# print(library.get_statistics())
