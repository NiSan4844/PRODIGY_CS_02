import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
import random

class StaticEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Static Black-and-White Image Encryption and Decryption Tool")
        self.root.geometry("800x400")

        # Create frames for organization
        self.image_frame = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
        self.image_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.control_frame = tk.Frame(self.root, bd=2, relief=tk.RAISED)
        self.control_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        # Labels for displaying images
        self.original_image_label = tk.Label(self.image_frame, text="Original Image")
        self.original_image_label.pack()

        self.original_image_display = tk.Label(self.image_frame)
        self.original_image_display.pack()

        self.encrypted_image_label = tk.Label(self.image_frame, text="Encrypted Image (Static B&W)")
        self.encrypted_image_label.pack()

        self.encrypted_image_display = tk.Label(self.image_frame)
        self.encrypted_image_display.pack()

        self.decrypted_image_label = tk.Label(self.image_frame, text="Decrypted Image (Restored Color)")
        self.decrypted_image_label.pack()

        self.decrypted_image_display = tk.Label(self.image_frame)
        self.decrypted_image_display.pack()

        # Buttons
        self.select_button = tk.Button(self.control_frame, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=10)

        self.encrypt_button = tk.Button(self.control_frame, text="Encrypt Image", state=tk.DISABLED, command=self.encrypt_image)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(self.control_frame, text="Decrypt Image", state=tk.DISABLED, command=self.decrypt_image)
        self.decrypt_button.pack(pady=10)

        self.save_button = tk.Button(self.control_frame, text="Save Encrypted Image", state=tk.DISABLED, command=self.save_image)
        self.save_button.pack(pady=10)

        self.clear_button = tk.Button(self.control_frame, text="Clear", command=self.clear_images)
        self.clear_button.pack(pady=10)

        # Variables to hold image data
        self.original_image = None
        self.encrypted_image = None
        self.decrypted_image = None
        self.original_rgb = None  # Variable to store the original RGB values

    def select_image(self):
        """Open a file dialog to select an image and display it."""
        input_image_path = filedialog.askopenfilename()
        if input_image_path:
            self.original_image = Image.open(input_image_path).convert("RGB")
            self.display_image(self.original_image, self.original_image_display)
            self.encrypt_button.config(state=tk.NORMAL)

    def display_image(self, image, label):
        """Display an image on the specified label."""
        resized_image = image.resize((200, 200))  # Resize for display
        img_tk = ImageTk.PhotoImage(resized_image)
        label.img_tk = img_tk  # Keep a reference to avoid garbage collection
        label.config(image=img_tk)

    def encrypt_image(self):
        """Encrypt the image by creating a static black-and-white noise version."""
        if self.original_image:
            # Store original RGB values
            image_array = np.array(self.original_image)
            self.original_rgb = image_array.copy()  # Save original RGB values

            # Generate static black-and-white noise
            static_bw = np.zeros_like(image_array)
            for i in range(image_array.shape[0]):
                for j in range(image_array.shape[1]):
                    # Randomly assign either black or white pixel
                    if random.random() > 0.5:
                        static_bw[i, j] = [255, 255, 255]  # White
                    else:
                        static_bw[i, j] = [0, 0, 0]  # Black
            
            self.encrypted_image = Image.fromarray(static_bw.astype('uint8'), 'RGB')
            self.display_image(self.encrypted_image, self.encrypted_image_display)
            self.save_button.config(state=tk.NORMAL)
            self.decrypt_button.config(state=tk.NORMAL)

    def decrypt_image(self):
        """Decrypt the image and restore the original colors."""
        if self.original_rgb is not None:
            # Restore original colors using the stored RGB values
            self.decrypted_image = Image.fromarray(self.original_rgb.astype('uint8'), 'RGB')
            self.display_image(self.decrypted_image, self.decrypted_image_display)

    def save_image(self):
        """Save the encrypted (static black-and-white) image."""
        if self.encrypted_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
            if save_path:
                self.encrypted_image.save(save_path)
                messagebox.showinfo("Success", f"Image saved as {save_path}")

    def clear_images(self):
        """Clear the image displays."""
        self.original_image_display.config(image='')
        self.encrypted_image_display.config(image='')
        self.decrypted_image_display.config(image='')
        self.original_image = None
        self.encrypted_image = None
        self.decrypted_image = None
        self.original_rgb = None
        self.encrypt_button.config(state=tk.DISABLED)
        self.decrypt_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.DISABLED)

def create_gui():
    """Create and launch the GUI for the Static B&W Encryption Tool."""
    root = tk.Tk()
    app = StaticEncryptionApp(root)
    root.mainloop()

if __name__ == "__main__":
    create_gui()
