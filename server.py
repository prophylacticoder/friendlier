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

        if request.form.get('anonymous'):
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

        return redirect("http://localhost:5000", code=302)

@app.route('/friendliers', methods=['GET', ])
def handle_ajax():
    positionCounter = request.args.get('position', '')

    # Create a DB connection and set up a cursor
    con = db.sql_connection()
    cursorObj = con.cursor()

    positionCounter = int(positionCounter)

    selectMaxNumber = "SELECT max(id) FROM messages"

    cursorObj.execute(selectMaxNumber)

    rows = cursorObj.fetchall()

    positionCounter = rows[0][0] - positionCounter + 1

    print(positionCounter)

    selectStatement = """SELECT nickname, datePosted, message FROM messages
                        WHERE id <= {} AND id >= {} ORDER BY id DESC""".format(
                        (positionCounter), (positionCounter - 10))

    cursorObj.execute(selectStatement)

    rows = cursorObj.fetchall()
    con.close()

    json_str = json.dumps(rows)

    return json_str
