
# StegoX - Hide a Secret Text Message in an Image

This is a Python program that allows the user to hide a secret text message inside an image using the least significant bit (LSB) technique. The program uses the stegano library to perform the hiding and revealing of the message.

The program has a graphical user interface (GUI) built using the tkinter library. The GUI consists of four frames. The first frame displays the image that the user selects. The second frame is a text box where the user can enter the secret message. The third frame contains two buttons, one for opening an image file, and another for saving the hidden image. The fourth frame contains two buttons, one for hiding the secret message in the image, and another for revealing the hidden message from the image.

The program generates a private key and a public key using the hashlib and secrets libraries. The private key is used to encrypt the secret message before hiding it in the image. The public key is used to decrypt the hidden message from the image. The keys are saved in two separate text files named "Private_key.txt" and "Public_key.txt" in the current working directory.

When the user clicks on the "Hide Data" button, the program reads the secret message from the text box, generates a private key, encrypts the message using the private key, hides the encrypted message in the image using LSB, and saves the modified image in a folder named "Output".

When the user clicks on the "Show" button, the program reads the private key from the "Private_key.txt" file and the public key from the "Public_key.txt" file. If the keys match, the program reveals the hidden message from the image using LSB and decrypts it using the private key. If the keys do not match, an error message is displayed in the text box.

## Features

- Hide a secret text message in an image file.
- Retrieve a hidden message from an image file.
- Encrypt your private key using SHA256.
- Save the output image in the specified output folder.
- Open and save image files in PNG and JPG formats.
- User-friendly graphical interface using Tkinter.

## Requirements

- Python 3.x
- stegano
- tkinter
- pillow

## Installation

1. Install Python 3.x on your computer.
2. Install required packages by running the following command:

   ```
   pip install stegano tkinter pillow
   ```

3. Clone the repository or download the ZIP file.
4. Run the following command in your terminal to launch the application:

   ```
   python StegoX.py
   ```

## Usage

1. Open the image file in which you want to hide the message by clicking on the `Open Image` button.
2. Type the message you want to hide in the `Text Box`.
3. Click on the `Hide Data` button to hide the message.
4. Click on the `Save Image` button to save the modified image file in the output folder.
5. To retrieve the hidden message, click on the `Show` button.
6. If the private key is correct, the hidden message will appear in the `Text Box`.

## Note

- The private key is automatically generated when you click on the `Hide Data` button. It is stored in a file called `Private_key.txt` in the same directory as the program.
- The public key is generated at the same time as the private key and is stored in a file called `Public_key.txt` in the same directory as the program.
- When you click on the `Hide Data` button, the output image is automatically saved in the `Output` folder in the same directory as the program.
- The `Save Image` button allows you to save the output image in the same directory as the program.
- The `Open Image` button allows you to open image files in PNG and JPG formats.
- If you enter an incorrect private key, the `Text Box` will display an error message.

## License

This project is licensed under the GPL.
