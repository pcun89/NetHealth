"""
metrics.py

Bandwidth calculation logic.
"""


def computeBandwidth(prev, curr, elapsed):
    """
    Computes bandwidth.

    Formula:
    (curr - prev) / time

    Time Complexity: O(n)
    Data Structure: Dictionary
    """
    result = {}

    for ifIndex in curr:
        if ifIndex in prev:
            inRate = (curr[ifIndex][0] - prev[ifIndex][0]) / elapsed
            outRate = (curr[ifIndex][1] - prev[ifIndex][1]) / elapsed

            result[ifIndex] = (inRate, outRate)

    return result
