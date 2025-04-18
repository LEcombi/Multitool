
# Multitool

A versatile tool written in Python that provides various useful functionalities.

---

## Features

### 1. Password Generator
Generates secure passwords with a custom length. The generated password is automatically copied to the clipboard.

### 2. Text Repeater
Repeats a given text a specified number of times and copies the result to the clipboard.

### 3. YouTube Downloader
Downloads videos from YouTube and saves them to a specified folder.

### 4. System Information Display
Displays information about the operating system, hostname, IP address, and CPU architecture.

### 5. Host Ping
Allows you to ping an IP address or hostname with a custom number of attempts.

### 6. QR Code Generator
Creates QR codes from any data and saves them as image files.

### 7. Auto Clicker
Enables automatic clicking on a specified button (left or right) with a custom click rate (number of clicks per second).

### 8. Network Device Scanner
Scans a specified IP address range and displays the found devices (IP and MAC addresses).

### 9. Port Scanner
Scans a specified range of ports from a host, displays the open ports, and saves them into a .txt file.

---

## Requirements

Make sure to install the required dependencies by running the following commands:

```bash
pip install pyperclip
pip install yt-dlp
pip install qrcode
pip install scapy
pip install pynput
```

---

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/LEcombi/Multitool.git
   cd Multitool
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:
   ```bash
   python main.py
   ```

---

## Note on Using the **Scan-Network** Feature

The **Scan-Network** feature of the Multitool program requires elevated privileges because it accesses network resources that need administrator rights.

### Important Notes

- To successfully use the **Scan-Network** feature, run the program with **sudo** (on Linux) or as an administrator (on Windows).
- Without these privileges, the feature may not function correctly, or access may be denied.

---