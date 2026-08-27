#!/usr/bin/env python3
import ssl
import socket
import sys

def audit_ssl(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            cipher = ssock.cipher()
            version = ssock.version()
            print(f"Audit: {hostname}:{port}")
            print(f"  TLS Version: {version}")
            print(f"  Cipher: {cipher[0]}")
            print(f"  Subject: {cert.get('subject')}")
            print(f"  Issuer: {cert.get('issuer')}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ssl-auditor.py <hostname>")
        sys.exit(1)
    audit_ssl(sys.argv[1])
