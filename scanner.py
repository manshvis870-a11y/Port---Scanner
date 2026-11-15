# My First Cybersecurity Tool - Port Scanner
# Made by [Manshvi sharma] | BCA Student

import socket
from datetime import datetime

# 1. Ask user which website/IP to scan
target = input("Enter IP or Website to scan (e.g. 127.0.0.1): ")

print(f"\nScanning {target}...")
print(f"Started at: {datetime.now()}")
print("-" * 50)

try:
    # 2. Loop through first 100 ports
    for port in range(1, 101):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        
        # 3. Try to connect to the port
        result = s.connect_ex((target, port))
        
        # 4. If result is 0, port is OPEN
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        
        s.close()

except KeyboardInterrupt:
    print("\nYou stopped the scan.")
except socket.gaierror:
    print("Invalid Website/IP. Try again.")
except socket.error:
    print("Could not connect to server.")

print("-" * 50)
print("Scan Finished!")
