# Caesar Cipher Encryption & Decryption (Linux Bash Script and Python)

## 📌 Introduction
The **Caesar Cipher** is one of the simplest and most widely known encryption techniques. It is a **substitution cipher** where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.  

This Bash script allows users to **encrypt** and **decrypt** messages using the **Caesar Cipher algorithm** with a custom shift value. Additionally, all encrypted and decrypted messages are **automatically saved in a log file** for future reference.

---

## ⚙️ Features
✅ **Encrypt a message** using Caesar Cipher  
✅ **Decrypt a message** using the same shift value  
✅ **Automatic logging** of all encryption and decryption operations  
✅ **Persistent logs** (data is stored even after the script is closed)  
✅ **Simple command-line interface** for ease of use  

---

## 🛠️ Prerequisites
Before running this script, ensure that:  
- You have a **Linux-based system** (e.g., Kali Linux, Ubuntu, Debian).  
- You have **Bash installed** (default in most Linux systems).  
- You have basic knowledge of using the terminal.  

---

## 🚀 Features
- Encrypt and decrypt messages using the **Caesar Cipher** algorithm.
- Available in both **Bash** and **Python**.
- Saves all encrypted and decrypted messages automatically in an **Excel file**.
- Automatically loads previous records when restarted.

---

## 📌 Installation & Usage Guide

### Step 1: Download the Script
Clone this repository using Git:
```bash
git clone https://github.com/your-username/caesar-cipher.git
```
Or manually create the script file:
```bash
nano caesar_cipher.sh  # For Bash
nano caesar_cipher.py  # For Python
```
Copy and paste the respective script into the file and save.

### Step 2: Make the Script Executable (For Bash)
```bash
chmod +x caesar_cipher.sh
```

### Step 3: Run the Script
For Bash:
```bash
./caesar_cipher.sh
```
For Python:
```bash
python3 caesar_cipher.py
```

### Step 4: Encrypt or Decrypt a Message
1. Choose an option (1 for encryption, 2 for decryption, 3 to exit).
2. Enter your message (text to be encrypted or decrypted).
3. Enter the shift value (a number that determines the letter shift).
4. The script will display the result and save it in an Excel file.

#### Example:
```bash
Choose an option:
1. Encrypt a message
2. Decrypt a message
3. Exit
Enter your choice (1/2/3): 1
Enter the message to encrypt: HELLO
Enter the shift value: 3
Encrypted Message: KHOOR
```

---

## 🔧 Dependencies
### Bash Version:
- `awk`
- `tr`
- `sed`

### Python Version:
- `pandas`
- `openpyxl`

To install Python dependencies, run:
```bash
pip install pandas openpyxl
```

---

## 🛠 Tested On:
- **Ubuntu**
- **Debian**
- **Arch Linux**
- **Kali Linux**
- **Termux (for Bash version)**

---

## 📜 License
This project is licensed under the MIT License.

---

## 🤝 Contributing
Want to contribute? Fork the repo and submit a pull request.

---

## 📢 Find Me On:
<p align="left">
  <a href="https://github.com/your-username" target="_blank"><img src="https://img.shields.io/badge/Github-blue?style=for-the-badge&logo=github"></a>
</p>

---

## ⚠️ Disclaimer

<i>This project is created for educational purposes only. Unauthorized use of encryption to bypass security measures is illegal. Use this tool responsibly and ensure compliance with applicable laws.</i>

### 🎉 Thanks to all contributors!
