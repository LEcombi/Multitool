def auto_klicker(clicks_per_second=10, button=None):
    import threading
    import time
    from pynput.mouse import Button, Controller
    from pynput.keyboard import Listener, KeyCode

    # Settings
    click_delay = clicks_per_second

    if button == None:
        click_button = Button.left
    elif button == "left":
        click_button = Button.left
    elif button == "right":
        click_button = Button.right

    # Control buttons
    start_key = KeyCode(char='z')   # Start with "z"
    stop_key = KeyCode(char='x')    # Stop with "x"
    exit_key = KeyCode(char='q')    # end with "q"

    clicking = False
    program_running = True

    mouse = Controller()

    def clicker():
        while program_running:
            if clicking:
                mouse.click(click_button)
                time.sleep(click_delay)
            else:
                time.sleep(0.01)

    def on_press(key):
        global clicking, program_running
        if key == start_key:
            clicking = True
            print("▶️ AutoClicker has started")
        elif key == stop_key:
            clicking = False
            print("⏸️ AutoClicker has stopped")
        elif key == exit_key:
            clicking = False
            program_running = False
            print("❌ End AutoClicker...")
            return False

    # Start Klick-Thread
    click_thread = threading.Thread(target=clicker)
    click_thread.start()

    # Start Key recognition
    with Listener(on_press=on_press) as listener:
        listener.join()
