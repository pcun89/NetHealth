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
import os

# =====================================================
# Flask Setup
# =====================================================

app = Flask(__name__)

CORS(
    app,
    resources={r"/*": {"origins": "*"}}
)

socketio.init_app(
    app,
    cors_allowed_origins="*"
)

# =====================================================
# Database Initialization
# =====================================================

initDb()

# =====================================================
# Monitoring State
# =====================================================

monitoring_thread = None
monitoring_running = False

# =====================================================
# Routes
# =====================================================

@app.route("/")
def home():
    return {
        "message": "NetHealth API Running"
    }


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


@app.route("/api/status")
def status():
    return {
        "running": monitoring_running
    }


@app.route("/api/start-monitoring", methods=["POST"])
def start_monitoring():

    global monitoring_thread
    global monitoring_running

    if monitoring_running:
        return {
            "message": "Monitoring already running"
        }

    monitoring_running = True

    monitoring_thread = threading.Thread(
        target=pollLoop,
        daemon=True
    )

    monitoring_thread.start()

    return {
        "message": "Monitoring started"
    }


@app.route("/api/stop-monitoring", methods=["POST"])
def stop_monitoring():

    global monitoring_running

    monitoring_running = False

    return {
        "message": "Monitoring stopped"
    }


@app.route("/api/alerts")
def alerts():

    try:
        return jsonify(
            recentAlerts()
        )

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/api/metrics/<host>")
def metrics(host):

    try:
        return jsonify({
            "host": host,
            "metrics": recentMetrics(host)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# =====================================================
# Run Local Development
# =====================================================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            8080
        )
    )

    socketio.run(
        app,
        host="0.0.0.0",
        port=port
    )