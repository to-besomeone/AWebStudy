from flask import Flask, url_for

app = Flask(__name__)


@app.route('/hello/')
def hello_world():
    return 'Hello World!'

@app.route('/profile/<username>')
def get_profile(username):
    return 'profile : ' + username


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('hello_world'))
        print(url_for('get_profile', username='flask'))
