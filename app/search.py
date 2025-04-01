import sqlite3

def search_query(term):
    conn = sqlite3.connect('app/database.db')
    c = conn.cursor()
    c.execute("SELECT title, url, snippet FROM pages WHERE content LIKE ?", ('%' + term + '%',))
    results = c.fetchall()
    conn.close()
    return results
