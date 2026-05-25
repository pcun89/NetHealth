from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

from database import (
    initDb,
    recentAlerts,
    recentMetrics
)

from main import pollLoop

import threading

app = Flask(__name__)

CORS(app)

socketio = SocketIO(
    app,
    cors_allowed_origins="*"
)


@app.route("/")
def home():
    return "NetHealth API Running"


@app.route("/health")
def health():
    return {"status": "healthy"}


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
    socketio.emit(
        "metrics_update",
        data
    )


if __name__ == "__main__":

    # ✅ Initialize DB
    initDb()

    # ✅ Start polling thread
    threading.Thread(
        target=pollLoop,
        daemon=True
    ).start()

    # ✅ Start server
    socketio.run(
        app,
        host="0.0.0.0",
        port=8080
    )
