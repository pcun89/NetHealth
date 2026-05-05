"""
app.py

Flask API layer.
"""

from flask import Flask, jsonify
from flask_cors import CORS
from database import initDb, recentAlerts, recentMetrics

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    """
    Time Complexity: O(1)
    """
    return "NetHealth API Running"


@app.route("/health")
def health():
    """
    Time Complexity: O(1)
    """
    return {"status": "healthy"}


@app.route("/api/alerts")
def alerts():
    """
    Time Complexity: O(n)
    """
    return jsonify(recentAlerts())


@app.route("/api/metrics/<host>")
def metrics(host):
    """
    Time Complexity: O(n)
    """
    return jsonify({
        "host": host,
        "metrics": recentMetrics(host)
    })


if __name__ == "__main__":
    initDb()
    app.run(host="0.0.0.0", port=5000)
