#!/bin/bash
echo "=== Vulnerability Scan ==="
if command -v apt &>/dev/null; then
    apt list --upgradable 2>/dev/null | grep -i security || echo "No security updates"
fi
