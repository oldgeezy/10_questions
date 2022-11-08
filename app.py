import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from datetime import datetime
from dateutil import tz

app = Flask(__name__)
app.config['SECRET_KEY'] = '0c75bc51d5702945afad76139f528fbd0f658395ddb89d7b'

def fix_time(posts):
    new_list = [];
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/Chicago')
    
    for post in posts:
        utc = datetime.strptime(post[1], '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=from_zone)
        central = utc.astimezone(to_zone)
        new_list.append(central.strftime('%Y-%m-%d %H:%M'))
    return new_list

def fix_posts(posts):
    fixed_times = fix_time(posts)
    new_list = [];
    i = 0

    for each in posts:
        new_list.append((each[0], fixed_times[i], each[2], each[3], each[4], each[5], each[6], each[7], each[8], each[9]))   
        i+=1
    return new_list

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM responses').fetchall()
    conn.close()
    posts = fix_posts(posts)
    return render_template('index.html', posts = posts)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        response_1 = request.form['response_1']
        response_2 = request.form['response_2']
        response_3 = request.form['response_3']
        response_4 = request.form['response_4']
        response_5 = request.form['response_5']
        response_6 = request.form['response_6']
        response_7 = request.form['response_7']
        response_8 = request.form['response_8']
        response_9 = request.form['response_9']
        response_10 = request.form['response_10']
        
#        if not response_1:
#            flash('Responses are required!')
#        elif not response_2:
#            flash('Responses are required!')
#        else:
        conn = get_db_connection()
        conn.execute('INSERT INTO responses (response_1, response_2, response_3, response_4, response_5, response_6, response_7, response_8, response_9, response_10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (response_1, response_2, response_3, response_4, response_5, response_6, response_7, response_8, response_9, response_10))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/about/')
def about():
    return render_template('about.html')