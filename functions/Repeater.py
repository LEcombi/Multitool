def repeater():
    import pyperclip
    counter = 1

    Text = str(input("What would you like to write: "))
    TimesPrint = int(input("How many times would you like to write the text: "))

    # Here, the entire text is stored to be copied to the clipboard later
    entire_text = ""

    while counter < TimesPrint:
        entire_text += Text + "\n"  # Adds the text to entire_text
        counter += 1

    print(entire_text)
    print("The text has been copied to the clipboard.")

    # Copies the entire text to the clipboard
    pyperclip.copy(entire_text)