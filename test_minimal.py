from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!', 200

@app.route('/login')
def login_test():
    return 'Login Page', 200

if __name__ == '__main__':
    print("Starting minimal test app...", flush=True)
    sys.stdout.flush()
    app.run(host='127.0.0.1', port=5001, debug=False, threaded=True)
