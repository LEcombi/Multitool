import os
import dependencies.clear_screen as clear_screen
import dependencies.pause as pause

def ping_host():
    clear_screen.clear_screen()
    print("📶 === Ping Tool ===\n")
    
    host = input("🌍 Enter an IP address or domain: ")
    times_ping = str(input("🔁 Enter the number of times to ping (default is 4, type 0 for infinite): "))
    
    print("\n📡 Pinging...\n")

    if times_ping.strip() == "":
        os.system(f"ping -c 4 {host}" if os.name != 'nt' else f"ping {host}")
    elif times_ping == "0":
        os.system(f"ping {host}" if os.name != 'nt' else f"ping {host}")
    else:
        os.system(f"ping -c {times_ping} {host}" if os.name != 'nt' else f"ping {host}")

    print("\n✅ Ping completed.")
    pause.pause()
