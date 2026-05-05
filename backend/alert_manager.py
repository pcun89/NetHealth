"""
alert_manager.py

Handles alert creation.
"""

import time
from database import addAlert


def pushAlert(severity, message):
    """
    Creates alert.

    Time Complexity: O(1)
    Data Structure: None
    """
    alertId = str(int(time.time()))

    addAlert(alertId, severity, int(time.time()), message)
