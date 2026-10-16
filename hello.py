from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
    result = '<p>Hello</p>'
    result += '<a href="https://python.org">Check out Python here</a>'
    return result
