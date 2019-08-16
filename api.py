from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
    return 'hello world'

if __name__ == ('__main__'):
    port = int(os.environ.get('PORT', 3000))
    app.run(host = '0.0.0.0', port = port,debug = False)