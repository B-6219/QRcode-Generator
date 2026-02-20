
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode
import base64


# -------------------- FUNCTIONS --------------------

def generate_qr():
    data = entry.get().strip()

    if not data:
        status_label.config(text="⚠ Please enter data first!", fg="orange")
        return

    try:
        size = int(size_entry.get())
    except:
        size = 300

    qr = qrcode.QRCode(
        version=None,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(
        fill_color=fg_color.get(),
        back_color=bg_color.get()
    )

    qr_img = qr_img.resize((size, size))
    img_tk = ImageTk.PhotoImage(qr_img)

    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    qr_label.current_image = qr_img  # store for saving

    status_label.config(text="✅ QR Code generated successfully!", fg="#1fed0c")


def generate_qr_from_file():
    file_path = filedialog.askopenfilename()

    if not file_path:
        return

    try:
        with open(file_path, "rb") as file:
            file_data = file.read()

        encoded_data = base64.b64encode(file_data).decode("utf-8")

        qr = qrcode.QRCode(
            version=None,
            box_size=10,
            border=4,
        )

        qr.add_data(encoded_data)
        qr.make(fit=True)

        try:
            size = int(size_entry.get())
        except:
            size = 300

        qr_img = qr.make_image(
            fill_color=fg_color.get(),
            back_color=bg_color.get()
        )

        qr_img = qr_img.resize((size, size))
        img_tk = ImageTk.PhotoImage(qr_img)

        qr_label.config(image=img_tk)
        qr_label.image = img_tk
        qr_label.current_image = qr_img  # store for saving

        status_label.config(text="📁 QR created from file!", fg="#1fed0c")

    except:
        status_label.config(text="⚠ File too large or error occurred!", fg="orange")


def save_qr():
    if not hasattr(qr_label, "current_image"):
        status_label.config(text="⚠ Generate a QR first!", fg="orange")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")]
    )

    if file_path:
        qr_label.current_image.save(file_path)
        status_label.config(text="💾 QR Code saved successfully!", fg="#1fed0c")


# -------------------- MAIN WINDOW --------------------

root = tk.Tk()
root.title("Advanced QR Code Generator")
root.geometry("650x750")
root.configure(bg="#0f172a")
root.resizable(False, False)


# -------------------- TITLE --------------------

title = tk.Label(
    root,
    text="QR Code Generator",
    bg="#0f172a",
    fg="#1fed0c",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)


# -------------------- INPUT --------------------

entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 14),
    bd=2
)
entry.pack(pady=10)


# -------------------- SIZE OPTION --------------------

size_label = tk.Label(
    root,
    text="QR Size (pixels):",
    bg="#0f172a",
    fg="white",
    font=("Arial", 12)
)
size_label.pack()

size_entry = tk.Entry(root, width=10)
size_entry.insert(0, "300")
size_entry.pack(pady=5)


# -------------------- COLOR OPTIONS --------------------

fg_color = tk.StringVar(value="black")
bg_color = tk.StringVar(value="white")

color_frame = tk.Frame(root, bg="#0f172a")
color_frame.pack(pady=10)

tk.Label(color_frame, text="Foreground:", bg="#0f172a", fg="white").grid(row=0, column=0, padx=10)
tk.Entry(color_frame, textvariable=fg_color, width=10).grid(row=0, column=1)

tk.Label(color_frame, text="Background:", bg="#0f172a", fg="white").grid(row=0, column=2, padx=10)
tk.Entry(color_frame, textvariable=bg_color, width=10).grid(row=0, column=3)


# -------------------- BUTTONS --------------------

btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=20)

generate_btn = tk.Button(
    btn_frame,
    text="Generate QR (Text)",
    bg="#1fed0c",
    fg="black",
    width=18,
    font=("Arial", 12, "bold"),
    command=generate_qr
)
generate_btn.grid(row=0, column=0, padx=8)

file_btn = tk.Button(
    btn_frame,
    text="Generate QR (File)",
    bg="#38bdf8",
    fg="black",
    width=18,
    font=("Arial", 12, "bold"),
    command=generate_qr_from_file
)
file_btn.grid(row=0, column=1, padx=8)

save_btn = tk.Button(
    btn_frame,
    text="Save QR",
    bg="white",
    fg="black",
    width=18,
    font=("Arial", 12, "bold"),
    command=save_qr
)
save_btn.grid(row=0, column=2, padx=8)


# -------------------- QR DISPLAY --------------------

qr_label = tk.Label(root, bg="#0f172a")
qr_label.pack(pady=20)


# -------------------- STATUS --------------------

status_label = tk.Label(
    root,
    text="",
    bg="#0f172a",
    fg="orange",
    font=("Arial", 11, "bold")
)
status_label.pack()


root.mainloop()