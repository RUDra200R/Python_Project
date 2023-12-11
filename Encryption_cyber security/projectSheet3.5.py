import tkinter
from tkinter import *

mainWindow = tkinter.Tk()
mainWindow.geometry('640x480')
mainWindow.title("Encryption by cipher method ")
mainWindow.config(bg="silver")

text = StringVar()
# shift_value = StringVar()


# class Encryption:


# def __init__(self, Text, Shift):
#     self.Text = Text
#     self.Shift = Shift

# def encrypt():
#     Text = text.get()
#     Shift = int(shift_value.get())
#
#     encrypted_text = ''
#     for char in Text:
#         if not char.isnumeric():
#             ascii_offset = ord('A') if char.isupper() else ord('a')
#             encrypt_char = chr((ord(char) - ascii_offset + Shift) % 26 + ascii_offset)
#             encrypted_text += encrypt_char
#             txt.insert(0.0, encrypted_text)
#         else:
#             encrypted_text += char
#             txt.insert(0.0, encrypted_text)
#     print(encrypted_text)
#     return encrypted_text
#

def encrypted():
    Text = text.get()
    Shift = int(shift_value.get())
    result = ""

    # traverse text
    for i in range(len(Text)):
        char = Text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + Shift-65) % 26 + 65)
            # txt.insert(0.0, result)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + Shift - 97) % 26 + 97)
            # txt.insert(0.0, result)
    # print(result)
    # print(Shift)
    txt.insert(0.0, result)
    return result

    # @staticmethod
# def encrypted():
#     input_value = Text
#     shift = int(shift_value.get())
#     encrypted = Encryption(input_value, shift)
#
#
# # @staticmethod
# def decrypted(self):
#     input_value = self.Text.get()
#     shift = int(shift_value.get())
#     decrypted = Encryption(input_value, -shift)


# obj = Encryption(text, shift)
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
b1 = Button(mainWindow, text='Encrypt', font=("Times New Roman""bold", 10), width=12, height=2, bg='silver', fg='brown', command=encrypted)
b1.grid(row=10, column=5, padx=305, pady=15)

# encrypted_output = Label(mainWindow, font=("ariel", 24), fg="black", bg="white", textvariable=text)
# encrypted_output.grid(row=12, column=5)

# Decryption button
# b2 = Button(mainWindow, text='Decrypt', font=("Times New Roman""bold", 10), width=12, height=2, bg='silver', fg='brown')
# b2.grid(row=11, column=5, padx=305, pady=15)

# output
# output_value = tkinter.StringVar(mainWindow)
# output_label = Label(mainWindow, font=("ariel", 24),width=10, fg="black", bg="white", textvariable=output_value,)
# output_label.grid(row=13, column=5)

txt = Text(mainWindow, width=37, height=2, wrap=WORD)
txt.grid(row=11, column=5)
mainWindow.mainloop()
