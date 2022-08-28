from flask import Flask

app = Flask(__name__)
@app.route('/')
def root():
    return "<p style=\"color: black;\">Hi World</p><br /><a href=\"/about\">About</a>"
@app.route('/about')
def print_html():
    return "<p>I was just taking a look at Python ;)</p><br/><a href=\"https://github.com/AntonyOnScript\" target=\"_blank\">@AntonyOnScript</a>"