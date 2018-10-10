from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/profile/<username>')
def get_profile(username):
    return 'profile : ' + username

@app.route('/message/<int:message_id>')
def get_message(message_id):
    return 'message_id : %d' % message_id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
