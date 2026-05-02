"""
snmp_client.py

Simulates SNMP polling.
"""

import random


def get_interfaces_bytes():
    """
    Simulates device metrics.

    Time Complexity: O(n interfaces)
    Data Structure: Dictionary
    """
    data = {}

    for i in range(1, 4):
        data[i] = (
            random.randint(1000, 100000),
            random.randint(1000, 100000)
        )

    return data
