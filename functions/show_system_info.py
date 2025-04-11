import platform
import socket
from dependencies.clear_screen import clear_screen
from dependencies.pause import pause

def show_system_info():
    clear_screen()
    print("=== System Information ===\n")
    print(f"Operating System : {platform.system()} {platform.release()}")
    print(f"Hostname         : {socket.gethostname()}")
    print(f"IP Address       : {socket.gethostbyname(socket.gethostname())}")
    print(f"CPU Architecture : {platform.machine()}")
    pause()
