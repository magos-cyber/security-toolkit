#!/usr/bin/env python3
"""Secret Scanner - Looks for common secrets in files."""

import os
import re
import sys

PATTERNS = {
    "AWS Access Key": r'(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}',
    "GitHub Token": r'ghp_[A-Za-z0-9]{36}',
    "Slack Token": r'xox[baprs]-[0-9a-zA-Z]{10,48}',
    "Private Key": r'-----BEGIN (RSA|EC|DSA|OPENSSH) PRIVATE KEY-----',
    "JWT": r'eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}',
    "Generic API Key": r'api[_-]?key\s*[:=]\s*["']?[A-Za-z0-9]{20,}',
}

def scan_file(filepath):
    """Scan a file for secrets."""
    findings = []
    try:
        with open(filepath, 'r', errors='ignore') as f:
            content = f.read()
        for name, pattern in PATTERNS.items():
            matches = re.findall(pattern, content)
            for match in matches:
                findings.append((name, match[:20] + "..." if len(str(match)) > 20 else match))
    except (OSError, UnicodeDecodeError):
        pass
    return findings

def main():
    if len(sys.argv) < 2:
        print("Usage: python secret_scanner.py <path>")
        sys.exit(1)
    
    target = sys.argv[1]
    total_findings = 0
    
    if os.path.isfile(target):
        findings = scan_file(target)
        for name, match in findings:
            print(f"[FOUND] {name}: {match}")
        total_findings = len(findings)
    else:
        for root, dirs, files in os.walk(target):
            for file in files:
                filepath = os.path.join(root, file)
                findings = scan_file(filepath)
                if findings:
                    print(f"
{filepath}:")
                    for name, match in findings:
                        print(f"  [FOUND] {name}: {match}")
                total_findings += len(findings)
    
    print(f"
Total findings: {total_findings}")

if __name__ == "__main__":
    main()
