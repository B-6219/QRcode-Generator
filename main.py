import tkinter as tk
from PIL import Image,ImageTk
import qrcode


def generate_qr():
    data = entry.get()
    if data:
        qr_img = qrcode.make(data)
        qr_img.save("my_qr.png")
        
        
        img = Image.open("my_qr.png")
        img = img.resize((200, 200)) 
        img_tk = ImageTk.PhotoImage(img)

        
        qr_label.config(image=img_tk)
        qr_label.image = img_tk  

        
        status_label.config(text="✅ QR Code generated successfully!")
    else:
        status_label.config(text="⚠ Please enter data to generate QR Code.")


root =tk.Tk()
root.geometry('500x500')
root.resizable(0,0)
root.config(background='black')
root.title('QRCode Generator')

user_label =tk.Label(text='Enter the Data:',bg="black", font=('tiimes new romman',30,'bold'),fg='#1fed0c')
user_label.pack()

entry = tk.Entry(root,width=50,bd=1,)
entry.pack()

submit = tk.Button(root, text='Create QrCode',fg='black',bg='#1fed0c',command=generate_qr)
submit.pack(pady=20)

#Label to show status (instead of messagebox)
status_label = tk.Label(root, text='', bg='black', fg='orange', font=('Arial', 10, 'bold'))
status_label.pack()

#Label to show QR code image
qr_label = tk.Label(root, bg='black')
qr_label.pack(pady=20)


root.mainloop()