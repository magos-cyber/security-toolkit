#!/usr/bin/env python3
import subprocess
import sys

CHECKS = [
    ("SSH Protocol", "grep '^Protocol 2' /etc/ssh/sshd_config"),
    ("Password Auth", "grep '^PasswordAuthentication no' /etc/ssh/sshd_config"),
    ("Root Login", "grep '^PermitRootLogin no' /etc/ssh/sshd_config"),
    ("UFW Enabled", "ufw status | grep -q 'Status: active'"),
    ("Fail2Ban Running", "systemctl is-active fail2ban"),
]

def run_check(name, command):
    try:
        subprocess.run(command, shell=True, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    passed = 0
    failed = 0
    for name, command in CHECKS:
        if run_check(name, command):
            print(f"[OK] {name}")
            passed += 1
        else:
            print(f"[FAIL] {name}")
            failed += 1
    print(f"\nResults: {passed} passed, {failed} failed")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
