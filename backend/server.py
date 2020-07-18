from flask import Flask, request
app = Flask(__name__)

with open("../frontend/index.html") as file:
    index = file.read()
file.close()
@app.route('/')
@app.route('/index.html')
def default_page():
    return index
message = dict()
message['anonymous'] = False
@app.route('/message', methods=['POST',])
def handle_message():
    if request.method == 'POST':
        if 'anonymous' in request.form.values():
            message['anonymous'] = True
        else: message['nickname'] = request.form['nickname']
        message['message'] = request.form['message']
        print(message)
    return index
