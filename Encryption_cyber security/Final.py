import tkinter
from tkinter import *

mainWindow = tkinter.Tk()
mainWindow.geometry('640x480')
mainWindow.title("Encryption by caesar cipher method ")
mainWindow.config(bg="silver")

text = StringVar()


def encrypt():
    encrypt_value.delete(0.0, END)
    Text = text.get()
    Shift = int(shift_value.get())

    encrypted_text = ''
    for char in Text:
        if not char.isnumeric():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypt_char = chr((ord(char) - ascii_offset + Shift) % 26 + ascii_offset)
            encrypted_text += encrypt_char
        else:
            encrypted_text += char
    encrypt_value.insert(0.0, encrypted_text)
    return encrypted_text


def decrypt():
    decrypt_value.delete(0.0, END)
    Text = text.get()
    Shift = int(shift_value.get())

    decrypted_text = ''
    for char in Text:
        if not char.isnumeric():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypt_char = chr((ord(char) - ascii_offset - Shift) % 26 + ascii_offset)
            decrypted_text += decrypt_char
        else:
            decrypted_text += char
    decrypt_value.insert(0.0, decrypted_text)
    return decrypted_text


# Title
label_0 = Label(mainWindow, text="Encryption", width=25, font=("Times New Roman""bold", 30), background="silver")
label_0.grid(row=3, column=5, padx=300, pady=15)

# Text Entry Label
label_1 = Label(mainWindow, text="Write a word for Encryption", width=10,
                font=("Times New Roman""bold", 14), background="silver")
label_1.grid(row=7, column=5, ipadx=200, ipady=50)

# Text Box
entry_1 = Entry(mainWindow, font=("ariel", 24), fg="black", bg="white", textvariable=text)
entry_1.grid(row=8, column=5)


# shift
shift_value = tkinter.StringVar(mainWindow)
shift_value.set("3")
shift_option = tkinter.OptionMenu(mainWindow, shift_value, "1", "2", "3", "4", "5", '6', '7', '8', '9', '10')
shift_option.grid(column=5)


# Encryption  button
b1 = Button(mainWindow, text='Encrypt', font=("Times New Roman""bold", 10), width=12, height=2, bg='silver', fg='brown', command=encrypt)
b1.grid(row=10, column=5, padx=305, pady=15)


# Decryption button
b2 = Button(mainWindow, text='Decrypt', font=("Times New Roman""bold", 10), width=12, height=2, bg='silver', fg='brown', command=decrypt)
b2.grid(row=11, column=5, padx=305, pady=15)

# output
encrypt_value = Text(mainWindow, font="Bold", width=37, height=1, wrap=WORD)
encrypt_value.grid(row=12, column=5)

decrypt_value = Text(mainWindow,font='Bold', width=37, height=1, wrap=WORD)
decrypt_value.grid(row=15, column=5)

mainWindow.mainloop()
