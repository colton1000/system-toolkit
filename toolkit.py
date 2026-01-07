import os
import platform
import shutil
import tempfile
import socket
import subprocess
import urllib.request

def clear_temp():
    temp_dir = tempfile.gettempdir()
    try:
        shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)
        print("[✓] Temporary files cleared.")
    except Exception as e:
        print(f"[!] Error clearing temp files: {e}")

def system_info():
    print("\n=== System Information ===")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Python Version: {platform.python_version()}")
    print("==========================\n")

def ping_test(target="8.8.8.8"):
    print(f"\n=== Ping Test ({target}) ===")
    try:
        # Windows uses '-n', Linux/Mac use '-c'
        count_flag = "-n" if platform.system().lower() == "windows" else "-c"
        result = subprocess.run(
            ["ping", count_flag, "4", target],
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except Exception as e:
        print(f"[!] Ping test failed: {e}")

def local_network_info():
    print("\n=== Local Network Info ===")
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"Local IP: {local_ip}")
    except Exception as e:
        print(f"[!] Error getting local network info: {e}")

def external_ip():
    print("\n=== External IP ===")
    try:
        ip = urllib.request.urlopen("https://api.ipify.org").read().decode()
        print(f"External IP: {ip}")
    except Exception as e:
        print(f"[!] Could not retrieve external IP: {e}")

def dns_test(domain="google.com"):
    print(f"\n=== DNS Test ({domain}) ===")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain} resolved to {ip}")
    except Exception as e:
        print(f"[!] DNS resolution failed: {e}")

def network_diagnostics():
    print("\n=== Network Diagnostics ===")
    local_network_info()
    external_ip()
    dns_test()
    ping_test()
    print("=== Diagnostics Complete ===\n")

def main():
    while True:
        print("\n=== System Toolkit ===")
        print("1. Clear Temp Files")
        print("2. Show System Info")
        print("3. Exit")
        print("4. Network Diagnostics")
        choice = input("Select an option: ")

        if choice == "1":
            clear_temp()
        elif choice == "2":
            system_info()
        elif choice == "3":
            print("Goodbye!")
            break
        elif choice == "4":
            network_diagnostics()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()