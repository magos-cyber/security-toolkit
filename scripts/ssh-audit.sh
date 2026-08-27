#!/bin/bash
# SSH Configuration Audit
# Checks SSH security settings

echo "=== SSH Audit ==="

# Check SSH config
if [ -f /etc/ssh/sshd_config ]; then
    echo "SSH Configuration:"
    
    # Protocol
    if grep -q "^Protocol 2" /etc/ssh/sshd_config; then
        echo "[OK] Protocol 2"
    else
        echo "[WARN] Protocol not explicitly set to 2"
    fi
    
    # Root login
    if grep -qi "^PermitRootLogin no" /etc/ssh/sshd_config; then
        echo "[OK] Root login disabled"
    else
        echo "[WARN] Root login may be enabled"
    fi
    
    # Password auth
    if grep -qi "^PasswordAuthentication no" /etc/ssh/sshd_config; then
        echo "[OK] Password auth disabled"
    else
        echo "[INFO] Password auth enabled"
    fi
    
    # Pubkey auth
    if grep -qi "^PubkeyAuthentication yes" /etc/ssh/sshd_config; then
        echo "[OK] Pubkey auth enabled"
    else
        echo "[WARN] Pubkey auth not enabled"
    fi
else
    echo "[FAIL] SSH config not found"
fi
