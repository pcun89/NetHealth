from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

from database import (
    initDb,
    recentAlerts,
    recentMetrics
)

app = Flask(__name__)

# ✅ Enables frontend communication
CORS(app)

# ✅ Enables WebSockets
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def home():
    """
    Home route

    Time Complexity: O(1)
    """
    return "NetHealth API Running"


@app.route("/health")
def health():
    """
    Health check

    Time Complexity: O(1)
    """
    return {"status": "healthy"}


@app.route("/api/alerts")
def alerts():
    """
    Returns alerts

    Time Complexity: O(n)
    Data Structure: List of dictionaries
    """
    return jsonify(recentAlerts())


@app.route("/api/metrics/<host>")
def metrics(host):
    """
    Returns metrics for host

    Time Complexity: O(n)
    """
    return jsonify({
        "host": host,
        "metrics": recentMetrics(host)
    })


def pushRealtimeUpdate(data):
    """
    Broadcasts realtime updates

    Time Complexity: O(n clients)
    Data Structure: JSON
    """
    socketio.emit("metrics_update", data)


if __name__ == "__main__":
    initDb()

    # ✅ Cloud Run requires port 8080
    socketio.run(app, host="0.0.0.0", port=8080)
