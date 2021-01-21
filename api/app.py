from flask import Flask
from flask_socketio import SocketIO, emit
import sys

app = Flask(__name__)
socketio = SocketIO(app)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        logging.error("Usage: app.py <service-port>")
        sys.exit(-1)
    p = int(sys.argv[1])
    socketio.run(app, host='0.0.0.0', port=p, debug=True)