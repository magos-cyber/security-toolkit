#!/usr/bin/env python3
import re
from collections import Counter

def analyze_auth_log(logfile="/var/log/auth.log"):
    failed_attempts = Counter()
    with open(logfile) as f:
        for line in f:
            if "Failed password" in line:
                match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if match:
                    failed_attempts[match.group(1)] += 1
    print("Failed SSH attempts:")
    for ip, count in failed_attempts.most_common(10):
        print(f"  {ip}: {count} attempts")

if __name__ == "__main__":
    analyze_auth_log()
