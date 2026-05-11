"""
anomaly.py

Detect anomalies using Z-score
"""

import statistics


def detectAnomaly(values):
    """
    Detects anomalies.

    Z = (x - mean) / std

    Time Complexity: O(n)
    Data Structure: List
    """
    if len(values) < 5:
        return False

    mean = statistics.mean(values)
    std = statistics.stdev(values)

    if std == 0:
        return False

    latest = values[-1]
    z = (latest - mean) / std

    return abs(z) > 2  # threshold
