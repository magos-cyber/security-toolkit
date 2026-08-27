#!/bin/bash
echo "=== File Permissions Audit ==="
echo "World-writable:"
find / -perm -002 -type f -not -path "/proc/*" 2>/dev/null | head -5
echo "SUID:"
find / -perm -4000 -type f 2>/dev/null | head -5