#!/bin/bash
HOST="${1:?Usage: $0 <host>}"
PORTS="${2:-22,80,443,8080,8443}"

echo "Scanning $HOST..."
IFS=',' read -ra PORT_LIST <<< "$PORTS"

for port in "${PORT_LIST[@]}"; do
    timeout 1 bash -c "echo >/dev/tcp/$HOST/$port" 2>/dev/null && \
        echo "Port $port: OPEN" || echo "Port $port: CLOSED"
done
