def repeater():
    import pyperclip
    print("🔁 === Text Repeater ===\n")
    
    text = input("✍️ What would you like to write: ")
    times = int(input("🔢 How many times would you like to repeat the text: "))
    mode = input("🔄 Choose a mode (1 for new line, 2 for space): ")

    if mode == "1":
        repeated_text = (text + "\n") * times
    elif mode == "2":
        repeated_text = (text + " ") * times

    # 🖨️ Print and copy the result
    print("\n📄 Repeated Text:\n")
    print(repeated_text)
    pyperclip.copy(repeated_text)
    print("✅ The text has been copied to the clipboard.")
