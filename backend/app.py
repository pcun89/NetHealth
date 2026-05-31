from flask import Flask, jsonify
from flask_cors import CORS

from socket_manager import socketio

from database import (
    initDb,
    recentAlerts,
    recentMetrics
)

from main import pollLoop

import threading

app = Flask(__name__)

CORS(app)

# ✅ Initialize socketio
socketio.init_app(app)


@app.route("/")
def home():
    return "NetHealth API Running"


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


@app.route("/api/alerts")
def alerts():
    return jsonify(
        recentAlerts()
    )


@app.route("/api/metrics/<host>")
def metrics(host):
    return jsonify({
        "host": host,
        "metrics": recentMetrics(host)
    })


if __name__ == "__main__":

    initDb()

    # ✅ Start polling engine
    threading.Thread(
        target=pollLoop,
        daemon=True
    ).start()

    socketio.run(
        app,
        host="0.0.0.0",
        port=8080
    )
