#!/bin/bash
# Vulnerability Scanner
# Basic vulnerability checks for common services

echo "=== Vulnerability Scanner ==="

# Check for running services that might be vulnerable
echo "Checking exposed databases..."
if ss -tulnp | grep -q "3306"; then
    echo "WARNING: MySQL port 3306 is exposed"
fi

if ss -tulnp | grep -q "5432"; then
    echo "WARNING: PostgreSQL port 5432 is exposed"
fi

if ss -tulnp | grep -q "6379"; then
    echo "WARNING: Redis port 6379 is exposed"
fi

# Check for running SSH
if ! command -v fail2ban &>/dev/null; then
    echo "WARNING: fail2ban not installed"
fi

# Check SSL/TLS
echo "Checking SSL/TLS configuration..."
if command -v openssl &>/dev/null; then
    for host in "localhost:443" "127.0.0.1:443"; do
        if openssl s_client -connect "$host" 2>/dev/null | grep -q "Verify return code"; then
            echo "SSL/TLS OK for $host"
        fi
    done
fi

echo "Vulnerability scan complete"
