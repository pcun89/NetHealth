"""
database.py

Handles SQLite operations.
"""

import sqlite3

DB_NAME = "nethealth.db"


def getConnection():
    """
    Creates DB connection.

    Time Complexity: O(1)
    Data Structure: SQLite connection object
    """
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def initDb():
    """
    Initializes tables.

    Time Complexity: O(1)
    Data Structure: Tables (devices, metrics, alerts)
    """
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS metrics (
        host TEXT,
        ts INTEGER,
        ifIndex INTEGER,
        inBytes INTEGER,
        outBytes INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        alertId TEXT,
        severity TEXT,
        ts INTEGER,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()


def addMetrics(host, ts, ifIndex, inBytes, outBytes):
    """
    Inserts metrics.

    Time Complexity: O(1)
    Data Structure: Tuple → SQLite row
    """
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO metrics VALUES (?, ?, ?, ?, ?)",
        (host, ts, ifIndex, inBytes, outBytes)
    )

    conn.commit()
    conn.close()


def addAlert(alertId, severity, ts, message):
    """
    Inserts alert.

    Time Complexity: O(1)
    Data Structure: Tuple
    """
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO alerts VALUES (?, ?, ?, ?)",
        (alertId, severity, ts, message)
    )

    conn.commit()
    conn.close()


def recentAlerts(limit=20):
    """
    Fetch alerts.

    Time Complexity: O(n)
    Data Structure: List of dicts
    """
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM alerts
    ORDER BY ts DESC
    LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "alertId": r[0],
            "severity": r[1],
            "ts": r[2],
            "message": r[3]
        }
        for r in rows
    ]


def recentMetrics(host, limit=50):
    """
    Fetch metrics.

    Time Complexity: O(n)
    Data Structure: List of dicts
    """
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM metrics
    WHERE host = ?
    ORDER BY ts DESC
    LIMIT ?
    """, (host, limit))

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "host": r[0],
            "ts": r[1],
            "ifIndex": r[2],
            "inBytes": r[3],
            "outBytes": r[4]
        }
        for r in rows
    ]
