from flask import Flask, request, render_template, redirect, url_for
import database as db
import time
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def default_page():
    return render_template('index.html')

message = dict()

@app.route('/message', methods=['POST',])
def handle_message():
    if request.method == 'POST':
        # Take the data from the request and organize into a dictionary
        if 'anonymous' in request.form.values():
            message['nickname'] = "Anonymous"
        else: message['nickname'] = request.form['nickname']
        message['message'] = request.form['message']

        # Create a DB connection
        con = db.sql_connection()
        cursorObj = con.cursor()

        # Insert into the database the new friendlier
        cursorObj.execute("""INSERT INTO messages(nickname, message, datePosted)
                             VALUES(?, ?, ?)""", (message['nickname'],
                            message['message'],
                            time.strftime('%Y-%m-%d %H:%M:%S')))
        con.commit()
        con.close()

        return render_template('index.html')

@app.route('/friendliers', methods=['GET', ])
def handle_ajax():
    numberOfFriendliers = request.args.get('n', '')

    # Create a DB connection and set up a cursor
    con = db.sql_connection()
    cursorObj = con.cursor()

    cursorObj.execute("""SELECT nickname, datePosted, message FROM messages
                        WHERE id <= 10""")

    rows = cursorObj.fetchall()

    con.close()

    json_str = json.dumps(rows)

    return json_str
