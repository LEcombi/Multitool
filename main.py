import functions.youtube_downloader as youtube_downloader
import functions.password_generator as password_generator
import pyperclip
import functions.Repeater as repeater
import functions.show_system_info as show_system_info
import functions.ping_host as ping_host
import functions.qr_code_gen as qr_code_generator
import functions.barcode_gen as barcode_generator
import dependencies.banner as banner
import dependencies.clear_screen as clear_screen

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
    print("4. Generate a barcode")
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
    print("4. Back to Main Menu")
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
                
                length = int(input("Enter the desired password length (minimum 4): "))
                try:
                    password = password_generator.generate_password(length)
                    print(f"Generated password: {password}")
                    pyperclip.copy(password)
                    print("Password copied to clipboard.")
                except ValueError as e:
                    print(e)
            elif utilities_choice == 2:  # Repeat text
                repeater.repeater()
            elif utilities_choice == 3:  # Generate a QR code
                data = input("Enter the data to encode in the QR code: ")
                output_folder = input("Enter the output folder (default is 'qr_codes'): ") or "qr_codes"
                file_name = input("Enter the file name (default is 'qr_code.png'): ") or "qr_code.png"
                qr_code_generator.generate_qr_code(data, output_folder, file_name)
            elif utilities_choice == 4:  # Generate a barcode
                data = input("Enter the data to encode in the barcode: ")
                output_folder = input("Enter the output folder (default is 'barcodes'): ") or "barcodes"
                file_name = input("Enter the file name (default is 'barcode.png'): ") or "barcode.png"
                barcode_generator.generate_barcode(data, output_folder, file_name)
            elif utilities_choice == 5:  # Back to Main Menu
                clear_screen.clear_screen()
                banner.display_banner()
                break
            else:
                print("Invalid choice. Please try again.")

    # Networking Menu
    elif choice == 2:
        while True:
            clear_screen.clear_screen()
            banner.display_banner()
            networking_choice = choose_networking_option()
            if networking_choice == 1:  # Download YouTube video
                video_url = input("Enter the YouTube video URL: ")
                output_path = input("Enter the output path (default is 'yt_downloads'): ") or "yt_downloads"
                youtube_downloader.download_youtube_video(video_url, output_path)

            elif networking_choice == 2:  # Show system information
                show_system_info.show_system_info()

            elif networking_choice == 3:  # Ping a host
                host = input("Enter the host to ping: ")
                ping_host.ping_host(host)

            elif networking_choice == 4:  # Back to Main Menu
                clear_screen.clear_screen()
                banner.display_banner()
                break

            else:
                print("Invalid choice. Please try again.")

    # Exit the program
    elif choice == 3:
        clear_screen.clear_screen()
        banner.display_banner()
        print("Exiting the program.")
        exit(0)

    # Handle invalid main menu choice
    else:
        print("Invalid choice. Please try again.")