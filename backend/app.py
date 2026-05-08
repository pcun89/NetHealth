"""
app.py (WebSocket version)
"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from database import initDb, recentAlerts, recentMetrics

app = Flask(__name__)
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def home():
    return "NetHealth API Running"


@app.route("/api/alerts")
def alerts():
    return jsonify(recentAlerts())


@app.route("/api/metrics/<host>")
def metrics(host):
    return jsonify({
        "host": host,
        "metrics": recentMetrics(host)
    })


def pushRealtimeUpdate(data):
    """
    Sends real-time data to frontend

    Time Complexity: O(n clients)
    Data Structure: JSON broadcast
    """
    socketio.emit("metrics_update", data)


if __name__ == "__main__":
    initDb()
    socketio.run(app, host="0.0.0.0", port=5000)
