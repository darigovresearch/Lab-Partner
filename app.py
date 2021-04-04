# app.py is code that runs a flask web app for the user interface

from flask import Flask, render_template

app = Flask(__name__)
# line to prevent cache from not updating static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
