import tkinter as tk
from tkinter import filedialog, messagebox
from steganography import encode_image, decode_image

def select_image():
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.bmp")])
    entry_image_path.delete(0, tk.END)
    entry_image_path.insert(0, path)

def encode():
    img_path = entry_image_path.get()
    output_path = filedialog.asksaveasfilename(defaultextension=".png")
    secret = text_message.get("1.0", tk.END).strip()
    if encode_image(img_path, output_path, secret):
        messagebox.showinfo("Success", "Message hidden successfully!")

def decode():
    img_path = entry_image_path.get()
    message = decode_image(img_path)
    text_message.delete("1.0", tk.END)
    text_message.insert(tk.END, message)

# GUI setup
root = tk.Tk()
root.title("Steganography Tool")

tk.Label(root, text="Image File:").pack()
entry_image_path = tk.Entry(root, width=50)
entry_image_path.pack()
tk.Button(root, text="Browse", command=select_image).pack()

tk.Label(root, text="Secret Message:").pack()
text_message = tk.Text(root, height=10, width=50)
text_message.pack()

tk.Button(root, text="Encode Message", command=encode).pack(pady=5)
tk.Button(root, text="Decode Message", command=decode).pack()

root.mainloop()