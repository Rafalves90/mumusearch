from flask import Flask, render_template, request
from .search import search_query

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results')
def results():
    query = request.args.get('q', '')
    results = search_query(query)
    return render_template('results.html', query=query, results=results)
