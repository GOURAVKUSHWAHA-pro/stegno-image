import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import base64
import zipfile
import os

class ImageEncoderDecoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encoder/Decoder")

        self.selected_file_path = None

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # File Selection
        self.label_file = tk.Label(self.root, text="Select a File:")
        self.label_file.pack(pady=10)

        self.button_browse = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.button_browse.pack(pady=5)

        # Image Display
        self.label_image = tk.Label(self.root, text="Selected Image will be displayed here.")
        self.label_image.pack(pady=10)

        # Encode/Decode Buttons
        self.button_encode = tk.Button(self.root, text="Encode", command=self.encode_file)
        self.button_encode.pack(pady=5)

        self.button_decode = tk.Button(self.root, text="Decode", command=self.decode_file)
        self.button_decode.pack(pady=5)

    def browse_file(self):
        self.selected_file_path = filedialog.askopenfilename(initialdir="/", title="Select File",
                                                              filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        self.label_file.config(text=f"Selected File: {os.path.basename(self.selected_file_path)}")

        # Display selected image
        self.display_image()

    def display_image(self):
        if self.selected_file_path:
            img = Image.open(self.selected_file_path)
            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(img)
            self.label_image.config(image=img)
            self.label_image.image = img

    def encode_file(self):
        if self.selected_file_path:
            with open(self.selected_file_path, 'rb') as file:
                file_content = file.read()

            # Encode the file content using base64
            encoded_content = base64.b64encode(file_content)

            # Save the encoded content to an image
            image_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            with open(image_path, 'wb') as img_file:
                img_file.write(encoded_content)

            tk.messagebox.showinfo("Encoding Complete", "File has been encoded and saved as an image.")

    def decode_file(self):
        if self.selected_file_path:
            # Open the image
            with open(self.selected_file_path, 'rb') as img_file:
                encoded_content = img_file.read()

            # Decode the content from base64
            decoded_content = base64.b64decode(encoded_content)

            # Save the decoded content to a file
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            with open(file_path, 'wb') as file:
                file.write(decoded_content)

            tk.messagebox.showinfo("Decoding Complete", "Image has been decoded and saved as a file.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncoderDecoderApp(root)
    root.mainloop()
