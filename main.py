import functions.youtube_downloader as youtube_downloader
import functions.password_generator as password_generator
import pyperclip
import functions.Repeater as repeater
import functions.show_system_info as show_system_info
import functions.ping_host as ping_host
import functions.qr_code_gen as qr_code_generator
import functions.barcode_gen as barcode_generator

def display_banner():
    banner = r"""
 _      _     _     _____  _  _____  ____  ____  _    
/ \__/|/ \ /\/ \   /__ __\/ \/__ __\/  _ \/  _ \/ \   
| |\/||| | ||| |     / \  | |  / \  | / \|| / \|| |   
| |  ||| \_/|| |_/\  | |  | |  | |  | \_/|| \_/|| |_/\
\_/  \|\____/\____/  \_/  \_/  \_/  \____/\____/\____/
                                                      
    """
    print(banner)


display_banner()

def choose_option():
    print("Please choose an option:")
    print("1. Generate a password")
    print("2. Repeat text")
    print("3. Download YouTube video")
    print("4. Show system information")
    print("5. Ping a host")
    print("6. Generate a QR code")
    print("7. Generate a barcode")
    print("8. Exit")
    choice = input("Enter your choice: ")
    return int(choice)

choice = choose_option()

while True:
    if choice == 1:
        length = int(input("Enter the desired password length (minimum 4): "))
        try:
            password = password_generator.generate_password(length)
            print(f"Generated password: {password}")
            pyperclip.copy(password)
            print("Password copied to clipboard.")
        except ValueError as e:
            print(e)
        break
    elif choice == 2:
        repeater.repeater()
        break
    elif choice == 3:
        video_url = input("Enter the YouTube video URL: ")
        output_path = input("Enter the output path (default is 'yt_downloads'): ") or "yt_downloads"
        youtube_downloader.download_youtube_video(video_url, output_path)
        break
    elif choice == 4:
        show_system_info.show_system_info()
        break
    elif choice == 5:
        ping_host.ping_host()
        break
    elif choice == 6:
        data = input("Enter the data to encode in the qr code: ")
        output_folder = input("Enter the output folder (default is 'qr_codes'): ") or "qr_codes"
        file_name = input("Enter the file name (default is 'qr_code.png'): ") or "barcode.png"
        qr_code_generator.generate_qr_code(data, output_folder, file_name)

    elif choice == 7:
        data = input("Enter the data to encode in the barcode: ")
        output_folder = input("Enter the output folder (default is 'barcodes'): ") or "barcodes"
        file_name = input("Enter the file name (default is 'barcode.png'): ") or "barcode.png"
        barcode_generator.generate_barcode(data, output_folder, file_name)
    elif choice == 8:
        print("Exiting the program.")
        exit(0)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = choose_option()