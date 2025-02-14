from flask import Flask, request, jsonify
from flask_cors import CORS
from check_syntax import SQLParser

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def hello_name():
    data = request.get_json()
    print(data)
    result = check_syntax(data)
    return jsonify(result)

if __name__ == '__main__':

    app.run(debug=True)
