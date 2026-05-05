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

devices = ["192.168.1.1", "192.168.1.2"]


def pollDevice(device):
    """
    Polls a device.

    Time Complexity: O(n interfaces)
    Data Structure: Dictionary
    """
    prev = get_interfaces_bytes()

    while True:
        time.sleep(5)
        curr = get_interfaces_bytes()

        bandwidth = computeBandwidth(prev, curr, 5)

        for ifIndex, (inRate, outRate) in bandwidth.items():
            addMetrics(device, int(time.time()), ifIndex, inRate, outRate)

            if inRate > 80000:
                pushAlert("HIGH", f"{device} high inbound traffic")

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
