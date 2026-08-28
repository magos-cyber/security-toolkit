#!/usr/bin/env python3
"""Directory Permission Audit - Checks for insecure permissions."""

import os
import stat
import sys

def audit_directory(path, verbose=True):
    """Walk a directory and flag insecure permissions."""
    issues = []
    
    for root, dirs, files in os.walk(path):
        for item in dirs + files:
            full_path = os.path.join(root, item)
            try:
                st = os.stat(full_path)
                mode = stat.filemode(st.st_mode)
                perms = st.st_mode & 0o777
                
                # Group writable
                if perms & stat.S_IWGRP:
                    issues.append((full_path, "group-writable", mode))
                # World writable
                if perms & stat.S_IWOTH:
                    issues.append((full_path, "world-writable", mode))
            except OSError:
                pass
    
    if issues:
        for path, issue, mode in issues:
            print(f"WARNING: {path} - {issue} ({mode})")
    else:
        print("No permission issues found")
    
    return len(issues)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    audit_directory(target)
