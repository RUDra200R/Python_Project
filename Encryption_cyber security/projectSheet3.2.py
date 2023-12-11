import tkinter
from tkinter import *

mainWindow = tkinter.Tk()
mainWindow.geometry('640x480')
mainWindow.title("Encryption by cipher method ")
mainWindow.config(bg="silver")

text = StringVar()
shift = IntVar()


class Encryption:

    def __init__(self, text, shift):
        self.text = text
        self.shift = shift

    def encrypt(self):
        encrypted_text = ''
        for char in self.text:
            if char.isalpa():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                encrypt_char = chr((ord(char) - ascii_offset + self.shift) % 26 + ascii_offset)
                encrypted_text += encrypt_char
            else:
                encrypted_text += char
        return encrypted_text

    # @staticmethod
    def encrypted(self):
        input_value = entry_1.get()
        shift = int(shift_value.get())
        encrypted = Encryption(input_value, shift)
        output_label.set(encrypted)


    def decrypted(self):
        input_value = entry_1.get()
        shift = int(shift_value.get())
        decrypted = Encryption(input_value, -shift)
        output_label.set(decrypted)


# Title
label_0 = Label(mainWindow, text="Encryption", width=25, font=("Times New Roman""bold", 30), background="silver")
label_0.grid(row=3, column=5, padx=300, pady=15)

# Text Entry Label
label_2 = Label(mainWindow, text="Write a word for Encryption", width=10,
                font=("Times New Roman""bold", 14), background="silver")
label_2.grid(row=7, column=5, ipadx=200, ipady=50)

# Text Box
entry_1 = Entry(mainWindow, font=("ariel", 24), fg="black", bg="white", textvariable=text)
entry_1.grid(row=8, column=5)
# shift
shift_value = tkinter.StringVar(mainWindow)
shift_value.set("3")
shift_option = tkinter.OptionMenu(mainWindow, shift_value, "1", "2", "3", "4", "5", '6', '7', '8', '9', '10')
shift_option.grid(column=5)
# Encryption  button
b1 = Button(mainWindow, text='Encrypt', font=("Times New Roman""bold", 10), width=12, height=2, bg='silver', fg='brown')
b1.grid(row=10, column=5, padx=305, pady=15)

# encrypted_output = Label(mainWindow, font=("ariel", 24), fg="black", bg="white", textvariable=text)
# encrypted_output.grid(row=12, column=5)

# Decryption button
b2 = Button(mainWindow, text='Decrypt', font=("Times New Roman""bold", 10), width=12, height=2, bg='silver', fg='brown')
b2.grid(row=11, column=5, padx=305, pady=15)
# output
output_value = tkinter.StringVar(mainWindow)
output_label = Label(mainWindow, font=("ariel", 24), fg="black", bg="white", textvariable=output_value,)
output_label.grid(row=13, column=5)

mainWindow.mainloop()
