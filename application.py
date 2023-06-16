from flask import Flask, render_template
from random import choice

app = Flask(__name__)

@app.route("/")
def index():
    page = choice(['page_a.html', 'page_b.html'])
    return render_template(page)
