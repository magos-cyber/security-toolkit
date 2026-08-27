#!/bin/bash
# Firewall Audit
# Checks firewall status and rules

echo "=== Firewall Audit ==="

# Check UFW
if command -v ufw &>/dev/null; then
    echo "UFW Status:"
    ufw status verbose
fi

# Check iptables
if command -v iptables &>/dev/null; then
    echo ""
    echo "iptables Rules:"
    iptables -L -n --line-numbers | head -20
fi

# Check firewalld
if command -v firewall-cmd &>/dev/null; then
    echo ""
    echo "firewalld Status:"
    firewall-cmd --state 2>/dev/null || echo "Not running"
fi
