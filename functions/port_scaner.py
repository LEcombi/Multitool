# Portions of this code are based on work by Yuval Simon (https://github.com/yuvalsimon)
# Licensed under the MIT License – see LICENSE.txt for full license text.

import socket
import subprocess
import sys
import time
import os
import threading
from colorama import Fore, Style, init

# Automatisches Zurücksetzen der Farben nach jeder Ausgabe
init(autoreset=True)

class scanner:
    def __init__(self):
        subprocess.call('clear', shell=True)
        self.server = input(f"{Fore.BLUE}[CONSOLE] Enter IP/domain to scan: ")
        self.thr = int(input("Please enter number of threads: "))
        self.to_scan = str(input("How many ports to scan (1k-10k): "))

        if self.to_scan == '1k':
            self.to_scan = 1000
        elif self.to_scan == '10k':
            self.to_scan = 10000
        else:
            self.to_scan = int(self.to_scan)
        self.server_ip = socket.gethostbyname(self.server)

        # Ordner für Ausgabe erstellen
        if not os.path.exists('PortScanner'):
            os.makedirs('PortScanner')
        try:
            os.remove('PortScanner/open_ports.txt')
        except:
            pass

        self.f = open('PortScanner/open_ports.txt', 'a+')
        self.good = 0

        print('\n\nStarting scan...')
        time.sleep(1)
        subprocess.call('clear', shell=True)

        print(f"{Fore.YELLOW}[CONSOLE] Target's IP: {self.server_ip}\n")
        print('-' * 30)
        print('\n')

    def scan(self, p):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            r = sock.connect_ex((self.server_ip, p))
            if r == 0:
                print(f'{Fore.GREEN}[CONSOLE] Found open port: {p}')
                self.f.write(f"Found open port: {p}\n")
                self.good += 1
            sock.close()

        except KeyboardInterrupt:
            subprocess.call('clear', shell=True)
            print("Exiting as you wish...")
            sys.exit(0)

        except socket.gaierror:
            print(f'{Fore.RED}[ERROR] Hostname could not be resolved.')
            sys.exit(1)

        except socket.error:
            print(f'{Fore.RED}[ERROR] Could not connect to server.')
            sys.exit(1)

    def main(self):
        threads = []
        for p in range(1, self.to_scan + 1):
            while threading.active_count() > self.thr:
                time.sleep(0.01)
            t = threading.Thread(target=self.scan, args=(p,))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        self.f.close()

        if self.good == 0:
            print(f"{Fore.RED}[CONSOLE] No ports open.")
            print("Press enter to continue...")
            input()
        else:
            print(f"{Fore.YELLOW}[CONSOLE] Found {self.good} open ports out of {self.to_scan}")
            print(f"{Fore.YELLOW}[CONSOLE] Results saved in PortScanner/open_ports.txt")
            print("Press enter to continue...")
            input()
        print(Style.RESET_ALL)
