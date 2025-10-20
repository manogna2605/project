from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import geocoder

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('danger_pressed')
def handle_danger(data):
    # Optional: auto-detect sender location (approx)
    g = geocoder.ip('me')
    location = g.latlng if g.ok else [None, None]

    emit('alert_all', {
        'sender': data.get('sender', 'Someone'),
        'location': location
    }, broadcast=True)

if __name__ == '__main__':
    from flask_socketio import SocketIO
    socketio = SocketIO(app)
    socketio.run(app, host='0.0.0.0', port=10000, allow_unsafe_werkzeug=True)





