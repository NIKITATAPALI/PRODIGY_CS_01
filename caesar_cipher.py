import os
import pandas as pd

def load_existing_data(file_name):
    if os.path.exists(file_name):
        try:
            return pd.read_excel(file_name)
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame(columns=["Type", "Message", "Shift", "Result"])
    else:
        return pd.DataFrame(columns=["Type", "Message", "Shift", "Result"])

def save_data_to_excel(data, file_name):
    try:
        data.to_excel(file_name, index=False)
        print(f"Data successfully saved to {file_name}.")
    except Exception as e:
        print(f"Error saving data: {e}")

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    file_name = "caesar_cipher_logs.xlsx"
    data = load_existing_data(file_name)

    print("Welcome to the Caesar Cipher Program!")
    
    try:
        while True:
            print("\nChoose an option:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            print("3. Exit")
            
            choice = input("Enter your choice (1/2/3): ")
            if choice == '1':
                message = input("Enter the message to encrypt: ")
                shift = int(input("Enter the shift value: "))
                encrypted_message = caesar_cipher_encrypt(message, shift)
                print(f"Encrypted Message: {encrypted_message}")
                
                new_entry = pd.DataFrame([{
                    "Type": "Encryption",
                    "Message": message,
                    "Shift": shift,
                    "Result": encrypted_message
                }])
                data = pd.concat([data, new_entry], ignore_index=True)
            elif choice == '2':
                message = input("Enter the message to decrypt: ")
                shift = int(input("Enter the shift value: "))
                decrypted_message = caesar_cipher_decrypt(message, shift)
                print(f"Decrypted Message: {decrypted_message}")
                
                new_entry = pd.DataFrame([{
                    "Type": "Decryption",
                    "Message": message,
                    "Shift": shift,
                    "Result": decrypted_message
                }])
                data = pd.concat([data, new_entry], ignore_index=True)
            elif choice == '3':
                print("Saving data and exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        save_data_to_excel(data, file_name)

if __name__ == "__main__":
    main()

