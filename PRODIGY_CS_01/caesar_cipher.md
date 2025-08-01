# Task 01: Caesar Cipher Implementation

### Project Description
This project is an implementation of the Caesar Cipher, a simple and classic encryption technique. The program is a command-line tool that allows a user to encrypt and decrypt text by shifting each letter a specified number of places down the alphabet. The project was completed as part of the Prodigy Infotech Cybersecurity Internship.

### Tools and Technologies Used
* **Python 3**: The primary programming language.
* **Git**: Used for version control.
* **GitHub**: Hosted the project repository.
* **VScode**

### Key Features
* **Encryption**: Encrypts a message using a user-defined shift key.
* **Decryption**: Decrypts a message by reversing the shift.
* **Case Handling**: Preserves the case of letters (uppercase and lowercase).
* **Non-Alphabetic Character Handling**: Ignores numbers, spaces, and punctuation, leaving them unchanged.

### How to Run the Program
1.  **Clone the repository**:You can find the repository here: [Prodigy Infotech on GitHub](https://github.com/cyber-agentberry/Prodigy_InfoTech/blob/b5e3b45841851aea6d895fdf84346a746677365f/PRODIGY_CS_01/caesar.py).
   To clone it to your local machine, run the following command in your terminal:
    ```bash
    git clone [https://github.com/cyber-agentberry/Prodigy_InfoTech.git](https://github.com/cyber-agentberry/Prodigy_InfoTech.git)
    ```
3.  **Navigate to the project directory**:
    ```bash
    cd Prodigy_InfoTech/PRODIGY_CS_01
    ```
4.  **Run the Python script**:
    ```bash
    python caesar.py
    ```
5.  **Follow the on-screen prompts** to enter your message and the shift value for encryption or decryption.

### Code Structure
The program is structured with clear, modular functions:
* `caesar_cipher(text, shift, mode)`: A core function that handles both encryption and decryption based on the `mode` parameter.
* `main()`: The primary function that manages user input and calls the cipher function.

### Challenges and Learnings
* **Handling edge cases**: A key challenge was ensuring the cipher correctly handles cases like wrapping around the alphabet (e.g., shifting 'z' by 1 results in 'a'). This was solved using the modulo operator (`% 26`).
* **Command-line user interface**: I learned to create a simple, intuitive user interface for the program, including error handling for invalid user input (e.g., non-integer shift values).

### Future Improvements
* Add support for handling more complex characters, such as special characters from different languages.
* Implement a brute-force decryption feature that attempts all possible 25 shift values.
* Enhance the user interface with a more visually appealing design.

---
