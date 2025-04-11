import functions.youtube_downloader as youtube_downloader
import functions.password_generator as password_generator
import pyperclip
import functions.Repeater as repeater

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
    print("4. Exit")
    choice = input("Enter your choice (1,2 or 3): ")
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
        print("Exiting the program.")
        exit(0)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = choose_option()
