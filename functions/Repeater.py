def repeater():
    import pyperclip
    print("🔁 === Text Repeater ===\n")
    
    text = input("✍️ What would you like to write: ")
    times = int(input("🔢 How many times would you like to repeat the text: "))

    # 🧾 Store the repeated text
    repeated_text = (text + "\n") * times

    # 🖨️ Print and copy the result
    print("\n📄 Repeated Text:\n")
    print(repeated_text)
    pyperclip.copy(repeated_text)
    print("✅ The text has been copied to the clipboard.")
