#!/bin/bash
# Network Security Audit
# Reviews network configuration for security issues

echo "=== Network Security Audit ==="

# Check listening services
echo "--- Listening Services ---"
ss -tulnp | grep -E "127.0.0.1|0.0.0.0" | while read line; do
    if echo "$line" | grep -q "0.0.0.0"; then
        echo "WARNING: Service listening on 0.0.0.0"
        echo "  $line"
    fi
done

# Check firewall status
echo ""
echo "--- Firewall Status ---"
if command -v ufw &>/dev/null; then
    ufw status
else
    echo "UFW not installed"
fi

# Check for open ports
echo ""
echo "--- Open Ports (should be minimal) ---"
ss -tuln | grep LISTEN | awk '{print $4}' | awk -F: '{print $NF}' | sort -n | uniq

# Check routing
echo ""
echo "--- Routing Table ---"
ip route show | grep -E "default|0.0.0.0"

# Check DNS
echo ""
echo "--- DNS Servers ---"
cat /etc/resolv.conf | grep nameserver
