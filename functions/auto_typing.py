def auto_typing(text, delay=0.1):
    import keyboard
    import pyautogui
    import threading
    import time

    text_to_type = ""

    running = False

    def type_text():
        global running
        print("Wait 2 seconds...")
        time.sleep(2)
        print("Start typing...")
        while running:
            pyautogui.write(text_to_type)


    def start_typing():
        global running
        if not running:
            running = True
            threading.Thread(target=type_text, daemon=True).start()
            print("Start typing in 2 seconds...")

    def stop_typing():
        global running
        running = False
        print("Stop typing.")

    print("Press 'x' to start typing, 'y' to stop typing, and 'esc' to exit.")

    keyboard.add_hotkey('x', start_typing)
    keyboard.add_hotkey('y', stop_typing)
    keyboard.wait('esc')
