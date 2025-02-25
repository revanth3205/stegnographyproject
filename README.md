# Secure Image Steganography

This Python project implements a secure image steganography system, allowing users to hide secret messages within images using password protection.

## Features

* **Password Protection:** Encrypt and decrypt messages using a user-defined password, adding a layer of security.
* **Dynamic Message Length Handling:** The message length is automatically embedded within the image, eliminating the need for manual length input during decryption.
* **Simple and User-Friendly:** Easy-to-use command-line interface with clear prompts.
* **Visual Confirmation:** The encrypted image is automatically opened after successful encryption.
* **Uses OpenCV:** For image processing.

## Getting Started

### Prerequisites

* Python 3.x
* OpenCV (`pip install opencv-python`)

### Usage

1.  **Clone the Repository:**

    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```

2.  **Encryption:**

    ```bash
    python encrypt.py
    ```

    Follow the prompts to enter the secret message and password. The encrypted image will be saved as `revencrypted.jpg`.

3.  **Decryption:**

    ```bash
    python decrypt.py
    ```

    Follow the prompt to enter the password. The decrypted message will be displayed.

### File Descriptions

* `encrypt.py`: Contains the encryption script.
* `decrypt.py`: Contains the decryption script.
* `revanthproject.jpg`: (Example) Image file used for embedding the message.

## How it Works

The `encrypt.py` script:

1.  Reads the image `revanthproject.jpg`.
2.  Prepends the message length (as a 5-digit string) to the message itself.
3.  Embeds the message and length into the least significant bits (LSB) of the image's pixel values.
4.  Saves the modified image as `revencrypted.jpg`.
5.  Opens the encrypted image.

The `decrypt.py` script:

1.  Reads the encrypted image `revencrypted.jpg`.
2.  Prompts for the password.
3.  If the password is correct:
    * Extracts the message length from the first 5 LSB-embedded characters.
    * Extracts the message from the remaining LSB-embedded characters.
    * Displays the decrypted message.
4.  If the password is incorrect, displays an authentication error.

## Future Enhancements

* Implement stronger encryption algorithms (e.g., AES).
* Support for other file types (audio, video).
* Graphical User Interface (GUI).
* Error correction capabilities.
* Advanced steganalysis detection.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under the MIT License.
