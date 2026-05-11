"""
main.py

Polling engine.
"""

import time
import threading
from snmp_client import get_interfaces_bytes
from metrics import computeBandwidth
from database import addMetrics
from alert_manager import pushAlert
from app import pushRealtimeUpdate
from backend.anomaly import detectAnomaly

devices = ["192.168.1.1", "192.168.1.2"]

history = {}


def pollDevice(device):
    prev = get_interfaces_bytes()

    while True:
        time.sleep(5)
        curr = get_interfaces_bytes()

        bandwidth = computeBandwidth(prev, curr, 5)

        for ifIndex, (inRate, outRate) in bandwidth.items():

            key = f"{device}-{ifIndex}"

            if key not in history:
                history[key] = []

            history[key].append(inRate)

            # Keep last 20 values
            history[key] = history[key][-20:]

            # 🚨 AI DETECTION
            if detectAnomaly(history[key]):
                pushAlert(
                    "CRITICAL", f"Anomaly detected on {device} if {ifIndex}")

        prev = curr
        


def pollDevice(device):
    prev = get_interfaces_bytes()

    while True:
        time.sleep(5)
        curr = get_interfaces_bytes()

        bandwidth = computeBandwidth(prev, curr, 5)

        payload = []

        for ifIndex, (inRate, outRate) in bandwidth.items():
            addMetrics(device, int(time.time()), ifIndex, inRate, outRate)

            payload.append({
                "host": device,
                "ifIndex": ifIndex,
                "inBytes": inRate,
                "outBytes": outRate,
                "ts": int(time.time())
            })

        # 🔥 REAL-TIME PUSH
        pushRealtimeUpdate(payload)

        prev = curr


def pollLoop():
    """
    Starts threads.

    Time Complexity: O(n devices)
    Data Structure: Thread list
    """
    threads = []

    for device in devices:
        t = threading.Thread(target=pollDevice, args=(device,))
        t.start()
        threads.append(t)
