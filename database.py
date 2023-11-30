import sqlite3
from web_scrapper import scrape_all_pages
def create_db():
    connection = sqlite3.connect('outlets.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS outlets (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

# Function to store data in the database
def store_data(outlets):
    connection = sqlite3.connect('outlets.db')
    cursor = connection.cursor()
    cursor.executemany('INSERT INTO outlets (name, address) VALUES (?, ?)', outlets)
    connection.commit()
    connection.close()

# URL to scrape
url = 'https://zuscoffee.com/category/store/melaka'

# Scrape and store data
create_db()
outlets = scrape_all_pages(url)
print(outlets)
store_data(outlets)
print(f'{len(outlets)} outlets scraped and stored in the database.')