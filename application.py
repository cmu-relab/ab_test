from flask import Flask, render_template, request
from random import choice
from string import ascii_uppercase
import json, os

app = Flask(__name__)

@app.route("/")
def index():
    session = ''.join(choice(ascii_uppercase) for i in range(12))
    options = ['page_b.html', 'page_a.html']
    page = choice(options)
    return render_template(page, option=page, session=session)

@app.route('/store', methods=['POST'])
def store():
    # save the session data
    session = request.form['session']
    filepath = os.path.join(app.root_path, 'surveydata', session + '.json')
    json.dump(request.form, open(filepath, 'w+'))
    return render_template('demo.html', session=session)

@app.route('/finish', methods=['POST'])
def finish():
    # read the session data
    session = request.form['session']
    filepath = os.path.join(app.root_path, 'surveydata', session + '.json')
    data = json.load(open(filepath, 'r'))

    # uodate the record and save
    survey_code = ''.join(choice(ascii_uppercase) for i in range(12))
    data['survey_code'] = survey_code
    data.update(request.form)
    json.dump(data, open(filepath, 'w'))

    return render_template('finish.html', survey_code=survey_code)
