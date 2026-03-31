from flask import Flask
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count', 'Total Request Count')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return "Hello,Welcome to  DevOps : Fully Automated World  by Rahulraj !!!"

if __name__ == '__main__':
    start_http_server(8000)  # metrics on port 8000
    app.run(host='0.0.0.0', port=5000)
