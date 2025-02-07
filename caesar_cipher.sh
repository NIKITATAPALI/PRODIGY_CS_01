#!/bin/bash

LOG_FILE="caesar_cipher_logs.txt"

save_to_log() {
    echo "$1" >> "$LOG_FILE"
}

caesar_cipher_encrypt() {
    local text="$1"
    local shift="$2"
    local encrypted_text=""
    
    for ((i = 0; i < ${#text}; i++)); do
        char="${text:$i:1}"
        if [[ "$char" =~ [a-zA-Z] ]]; then
            base=$(printf '%d' "'$( [[ "$char" =~ [A-Z] ]] && echo 'A' || echo 'a' )")
            ascii=$(printf '%d' "'$char")
            new_ascii=$(( (ascii - base + shift) % 26 + base ))
            encrypted_text+=$(printf '\\x%x' "$new_ascii")
        else
            encrypted_text+="$char"
        fi
    done
    echo "$encrypted_text"
}

caesar_cipher_decrypt() {
    local text="$1"
    local shift="$2"
    caesar_cipher_encrypt "$text" $(( -shift ))
}

main() {
    echo "Welcome to the Caesar Cipher Program!"
    
    while true; do
        echo -e "\nChoose an option:"
        echo "1. Encrypt a message"
        echo "2. Decrypt a message"
        echo "3. Exit"
        
        read -p "Enter your choice (1/2/3): " choice
        
        if [[ "$choice" == "1" ]]; then
            read -p "Enter the message to encrypt: " message
            read -p "Enter the shift value: " shift
            encrypted_message=$(caesar_cipher_encrypt "$message" "$shift")
            echo "Encrypted Message: $encrypted_message"
            save_to_log "Encryption | Message: $message | Shift: $shift | Result: $encrypted_message"
        elif [[ "$choice" == "2" ]]; then
            read -p "Enter the message to decrypt: " message
            read -p "Enter the shift value: " shift
            decrypted_message=$(caesar_cipher_decrypt "$message" "$shift")
            echo "Decrypted Message: $decrypted_message"
            save_to_log "Decryption | Message: $message | Shift: $shift | Result: $decrypted_message"
        elif [[ "$choice" == "3" ]]; then
            echo "Exiting the program. Goodbye!"
            break
        else
            echo "Invalid choice. Please try again."
        fi
    done
}

main

