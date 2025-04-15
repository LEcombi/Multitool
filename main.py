import functions.youtube_downloader as youtube_downloader
import functions.password_generator as password_generator
import pyperclip
import functions.Repeater as repeater
import functions.show_system_info as show_system_info
import functions.ping_host as ping_host
import functions.qr_code_gen as qr_code_generator
import dependencies.banner as banner
import dependencies.clear_screen as clear_screen
import functions.List_network_devices as scan_network
from dependencies.screen_baner import reload
import functions.auto_klicker as auto_klicker

# Display the banner at the start of the program
banner.display_banner()

# Main menu function
def choose_option():
    print("\n" + "=" * 20)
    print("       Main Menu")
    print("=" * 20)
    print("1. Utilities")
    print("2. Networking")
    print("3. Exit")
    print("=" * 20)
    choice = input("Enter your choice: ")
    return int(choice)

# Utilities menu function
def choose_utilities_option():
    print("\n" + "=" * 20)
    print("   Utilities Menu")
    print("=" * 20)
    print("1. Generate a password")
    print("2. Repeat text")
    print("3. Generate a QR code")
    print("4. Auto Clicker")
    print("5. Back to Main Menu")
    print("=" * 20)
    choice = input("Enter your choice: ")
    return int(choice)

# Networking menu function
def choose_networking_option():
    print("\n" + "=" * 20)
    print("   Networking Menu")
    print("=" * 20)
    print("1. Download YouTube video")
    print("2. Show system information")
    print("3. Ping a host")
    print("4. Scan network devices")
    print("5. Back to Main Menu")
    print("=" * 20)
    choice = input("Enter your choice: ")
    return int(choice)

# Main program loop
while True:
    choice = choose_option()

    # Utilities Menu
    if choice == 1:
        clear_screen.clear_screen()
        banner.display_banner()
        while True:
            utilities_choice = choose_utilities_option()
            if utilities_choice == 1:  # Generate a password
                reload()
                length = int(input("Enter the desired password length (minimum 4): "))
                try:
                    password = password_generator.generate_password(length)
                    print(f"Generated password: {password}")
                    pyperclip.copy(password)
                    print("Password copied to clipboard.")
                except ValueError as e:
                    print(e)
            elif utilities_choice == 2:  # Repeat text
                reload()
                repeater.repeater()
            elif utilities_choice == 3:  # Generate a QR code
                reload()
                data = input("Enter the data to encode in the QR code: ")
                output_folder = input("Enter the output folder (default is 'qr_codes'): ") or "qr_codes"
                file_name = input("Enter the file name (default is 'qr_code.png'): ") or "qr_code.png"
                qr_code_generator.generate_qr_code(data, output_folder, file_name)
            elif utilities_choice == 4:  # Auto Clicker
                clicks_per_second = int(input("Enter the number of clicks per second (default is 10): ") or 10)
                button = input("Enter the button to click (left/right, default is left): ") or "left"
                auto_klicker.auto_klicker(clicks_per_second, button)
            elif utilities_choice == 5:  # Back to Main Menu
                reload()
                break
            else:
                print("Invalid choice. Please try again.")

    # Networking Menu
    elif choice == 2:
        while True:
            reload()
            networking_choice = choose_networking_option()
            if networking_choice == 1:  # Download YouTube video
                video_url = input("Enter the YouTube video URL: ")
                output_path = input("Enter the output path (default is 'yt_downloads'): ") or "yt_downloads"
                youtube_downloader.download_youtube_video(video_url, output_path)

            elif networking_choice == 2:  # Show system information
                reload()
                show_system_info.show_system_info()

            elif networking_choice == 3:  # Ping a host
                reload()
                host = input("Enter the host to ping: ")
                ping_host.ping_host(host)

            elif networking_choice == 4:  # Scan network devices
                reload()
                ip_range = input("Enter the IP range to scan: ")
                print(f"Scanning network: {ip_range}")

                devices = scan_network.scan_network(ip_range)
                if devices:
                    print(f"Found {len(devices)} devices:")
                    print("-" * 40)
                    for device in devices:
                        print(f"IP Address: {device['ip']}, MAC Address: {device['mac']}")
                else:
                    print("No devices found.")

            elif networking_choice == 5:  # Back to Main Menu
                reload()
                break

            else:
                print("Invalid choice. Please try again.")

    # Exit the program
    elif choice == 3:
        reload()
        print("Exiting the program.")
        exit(0)

    # Handle invalid main menu choice
    else:
        print("Invalid choice. Please try again.")