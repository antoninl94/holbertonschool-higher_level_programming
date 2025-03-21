#!/usr/bin/python3
"""
In this task we will build a basic Flask application that serves a web page using a Jinja template
"""
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open("./items.json", "r") as data:
        data = json.load(data)
        item_list = data['items']
        print(item_list)
    return render_template('items.html', items=item_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
