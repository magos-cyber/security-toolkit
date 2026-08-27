#!/bin/bash
echo "=== SSH Key Audit ==="
for user in $(cut -f1 -d: /etc/passwd); do
    home=$(eval echo ~$user 2>/dev/null)
    if [ -f "$home/.ssh/authorized_keys" ]; then
        echo "User: $user - Keys: $(wc -l < "$home/.ssh/authorized_keys")"
    fi
done