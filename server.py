from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def default_page():
    return render_template('index.html')

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
    return render_template('index.html')
