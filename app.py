# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/shutdown', methods=['POST'])
def shutdown():
   print("Shutting down gracefully...")
   os.kill(os.getpid(), signal.SIGINT)
   return 'Server shutting down...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)