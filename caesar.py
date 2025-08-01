def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a text using the Caesar Cipher method.
    Mode can be 'encrypt' or 'decrypt'.
    """
    if mode == 'decrypt':
        shift = -shift
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
                start = ord('a')
                shifted = (ord(char) - start + shift) % 26
                result += chr(start + shifted)
        elif 'A' <= char <= 'Z':
                start = ord('A')
                shifted = (ord(char) - start + shift) % 26
                result += chr(start + shifted)
        else:
             result += char
    return result

def main():
    while True:
        choice = input("Enter 'e' for encrypt, 'd' for decrypt, or 'q' for quit: ").lower()
        if choice == 'q':
            break

        if choice not in ['e', 'd']:
            print("Invalid choice. please enter 'e', 'd', or 'q'.")
            continue
        try:
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. please enter an integer.")
            continue

        mode = 'encrypt' if choice == 'e' else 'decrypt'
        processed_message = caesar_cipher(message, shift, mode)
        print(f"Processed message: {processed_message}")

if __name__ == "__main__":
        main()
    
