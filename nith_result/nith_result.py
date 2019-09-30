from flask import Blueprint, render_template

result = Blueprint('result',__name__,template_folder='templates',static_folder='static')

@result.route('/')
def home():
    return render_template('home.html')

from flask import Flask,request, jsonify, session, g, make_response
import json
import sqlite3

from flask import url_for

@result.route('/<string:rollno>/')
def get_result(rollno):
    rollno = rollno.lower()
    # return "ggod"
    conn = sqlite3.connect('mydb.db')
    cur = conn.execute('SELECT result FROM students WHERE rollno=(?)',(rollno,))
    result = cur.fetchone()
    if result is None:
        return "<h1>Roll no not in database.</h1>"
    else:
        result = json.loads(result[0])
        return render_template('result.html',tables=result)