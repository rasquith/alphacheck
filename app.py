from flask import Flask
from alphabet_check import has_alphabet
import json


app = Flask(__name__)


@app.route('/alphacheck')
def hello_world():
    return 'This is a RESTful web service. Append a string to the URL to ' \
           'see if it contains at least one of every character in the ' \
           'alphabet.'


@app.route('/alphacheck/<input_str>')
def process_string(input_str):
    return json.dumps({
        "data": {
            "valid": has_alphabet(input_str)
        }
    })


if __name__ == '__main__':
    app.run(debug=True)
