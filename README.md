
# Pixel Manipulation using Image Encryption and Decryption Tool

This project demonstrates a simple image encryption tool using static black-and-white pixel manipulation, built with Python. The tool allows users to encrypt an image by converting it into a black-and-white static image (similar to "noise") and then decrypt it to restore the original image with its colors. The GUI is implemented using the Tkinter library, with support for loading images, encrypting, decrypting, saving, and clearing them.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Code Walkthrough](#code-walkthrough)
4. [Key Functions](#key-functions)
5. [How to Run](#how-to-run)
6. [Future Improvements](#future-improvements)

---

## Overview

The **Static Black-and-White Image Encryption Tool** is a graphical interface application where users can:
- Load an image from their system.
- Encrypt the image using pixel manipulation (convert to static black-and-white).
- Decrypt the image to restore the original image with colors.
- Save the encrypted image.
- Clear the displayed images to start over.

The tool is simple and suitable for demonstrating basic image manipulation concepts like pixel manipulation and encryption.

---

## Features

- **Image Upload**: Select any image from your system.
- **Image Encryption**: Encrypt the image by generating a black-and-white noise pattern.
- **Image Decryption**: Restore the original image with colors.
- **Save Encrypted Image**: Save the encrypted image to your local system.
- **Clear Images**: Reset the display for all images (original, encrypted, decrypted).
- **GUI Interface**: Easy-to-use interface with buttons and image display areas.

---

## Code Walkthrough

### 1. **Setting Up the GUI**

```python
self.root = root
self.root.title("Static Black-and-White Image Encryption and Decryption Tool")
self.root.geometry("800x400")
```

- We initialize a Tkinter window with a title and set the dimensions of the main window to 800x400 pixels.

### 2. **Creating Frames for Image and Control Elements**

```python
self.image_frame = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
self.image_frame.pack(side=tk.LEFT, padx=10, pady=10)

self.control_frame = tk.Frame(self.root, bd=2, relief=tk.RAISED)
self.control_frame.pack(side=tk.RIGHT, padx=10, pady=10)
```

- The layout of the GUI is divided into two main sections: the left side for displaying images and the right side for control buttons (e.g., "Select Image", "Encrypt Image", "Decrypt Image", etc.). This helps in organizing the interface.

### 3. **Image Display Labels**

```python
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
```

- We create three labels to display the original image, encrypted image, and decrypted image. Each section has a title for user clarity.

### 4. **Control Buttons**

```python
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
```

- Buttons for performing actions like selecting, encrypting, decrypting, saving images, and clearing the displays are added. Initially, the "Encrypt", "Decrypt", and "Save" buttons are disabled until a valid image is selected.

---

## Key Functions

### 1. **Select Image**

```python
def select_image(self):
    input_image_path = filedialog.askopenfilename()
    if input_image_path:
        self.original_image = Image.open(input_image_path).convert("RGB")
        self.display_image(self.original_image, self.original_image_display)
        self.encrypt_button.config(state=tk.NORMAL)
```

- Allows the user to select an image file from their system. The image is converted to RGB and displayed in the original image section. Once an image is loaded, the "Encrypt Image" button becomes active.

### 2. **Display Image**

```python
def display_image(self, image, label):
    resized_image = image.resize((200, 200))
    img_tk = ImageTk.PhotoImage(resized_image)
    label.img_tk = img_tk
    label.config(image=img_tk)
```

- Resizes the image to 200x200 pixels for display purposes and updates the label with the image.

### 3. **Encrypt Image (Static Black-and-White Noise)**

```python
def encrypt_image(self):
    image_array = np.array(self.original_image)
    self.original_rgb = image_array.copy()

    static_bw = np.zeros_like(image_array)
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            if random.random() > 0.5:
                static_bw[i, j] = [255, 255, 255]
            else:
                static_bw[i, j] = [0, 0, 0]
    
    self.encrypted_image = Image.fromarray(static_bw.astype('uint8'), 'RGB')
    self.display_image(self.encrypted_image, self.encrypted_image_display)
    self.save_button.config(state=tk.NORMAL)
    self.decrypt_button.config(state=tk.NORMAL)
```

- This function generates a static black-and-white noise image by randomly assigning either a black or white value to each pixel. The original image's RGB values are stored for later decryption.

### 4. **Decrypt Image**

```python
def decrypt_image(self):
    if self.original_rgb is not None:
        self.decrypted_image = Image.fromarray(self.original_rgb.astype('uint8'), 'RGB')
        self.display_image(self.decrypted_image, self.decrypted_image_display)
```

- Restores the original colors of the image by using the previously stored RGB values and displays the decrypted image.

### 5. **Save Image**

```python
def save_image(self):
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
    if save_path:
        self.encrypted_image.save(save_path)
        messagebox.showinfo("Success", f"Image saved as {save_path}")
```

- Allows the user to save the encrypted (static black-and-white) image to their local system in either JPEG or PNG format.

### 6. **Clear Images**

```python
def clear_images(self):
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
```

- Clears all the displayed images and resets the state of the application to its initial form.

---

## How to Run

### Prerequisites
- Python 3.x
- Install required libraries: `Pillow`, `Tkinter`, and `numpy`
  
  You can install them using:
  ```bash
  pip install pillow numpy
  ```

### Steps
1. Run the Python script using:
   ```bash
   python image_encryption_tool.py
   ```
2. The GUI will open.
3. Select an image using the "Select Image" button.
4. Encrypt the image to see the static black-and-white version.
5. Decrypt the image to restore the original colors.
6. Save the encrypted image if needed.
7. Use the "Clear" button to reset the images.

---

## Future Improvements

- **Advanced Encryption**: Implement more sophisticated encryption techniques like pixel shuffling or XOR operations.
- **Progress Indicator**: Add a progress bar to show the encryption/decryption process in case of large images.
- **Batch Processing**: Add support for encrypting/decrypting multiple images at once.
- **Drag and Drop**: Allow users to drag and drop images into the GUI for easier file selection.

---

This tool is a good starting point for understanding pixel manipulation and how images can be altered using simple operations.