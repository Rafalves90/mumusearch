import requests
from bs4 import BeautifulSoup
import sqlite3

def crawl_and_store(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else url
    text = soup.get_text().strip().replace('\n', ' ')
    snippet = text[:200]

    conn = sqlite3.connect('app/database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pages
                 (title TEXT, url TEXT, snippet TEXT, content TEXT)''')
    c.execute("INSERT INTO pages VALUES (?, ?, ?, ?)", (title, url, snippet, text))
    conn.commit()
    conn.close()
