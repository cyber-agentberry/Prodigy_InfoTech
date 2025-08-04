from PIL import Image
import numpy as np
def encrypt_decrypt_image(image_path, key):
    """
    Encrypts or decrypts an image using a simple XOR cipher.
    This function performs both encryption and decryption.
    """
    try:
        # Open the image and convert it to a NumPy array
        img = Image.open(image_path)
        img_array = np.array(img)

        processed_array = img_array ^ key
        processed_img = Image.fromarray(processed_array.astype(np.uint8))
        return processed_img
    except FileNotFoundError:
        print(f"Error: The file at {image_path} was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
def main():
    while True:
        print("\n--- Simple Image Encryptor/Decryptor ---")
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()

        if choice == 'q':
            print("Exiting tool. Goodbye!")
            break

        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")
            continue

        try:
            input_path = input("Enter the path to the image file: ")
            key = int(input("Enter the encryption/decryption key (an integer): "))

            processed_img = encrypt_decrypt_image(input_path, key)

            if processed_img:
                output_path = input("Enter the path to save the new image: ")
                processed_img.save(output_path)
                print(f"Success! The image has been processed and saved to {output_path}")

        except ValueError:
            print("Invalid key. Please enter an integer.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()