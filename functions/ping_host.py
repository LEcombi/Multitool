import os
import dependencies.clear_screen as clear_screen
import dependencies.pause as pause

def ping_host():
    clear_screen.clear_screen()
    print("=== Ping Tool ===\n")
    host = input("Enter an IP address or domain: ")
    print("\nPinging...\n")
    os.system(f"ping -c 4 {host}" if os.name != 'nt' else f"ping {host}")
    pause.pause() 