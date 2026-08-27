#!/bin/bash
HOST="${1:?Usage: $0 <host>}"
PORT="${2:-443}"
echo "=== TLS Check: $HOST:$PORT ==="
echo | openssl s_client -connect "$HOST:$PORT" 2>/dev/null | openssl x509 -noout -dates -subject 2>/dev/null
