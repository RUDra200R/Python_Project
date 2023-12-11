import os
import tkinter
from tkinter import *

mainWindow = tkinter.Tk()
mainWindow.geometry('600x500')
mainWindow.title("Virtual Speaker")
mainWindow.config(bg="silver")

text = StringVar()


def execute():
    Text = text.get()
    command = f' mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""{Text}"")(window.close)")'
    print()
    os.system(command)
    entry_1.delete(0, END)


# Title
label_0 = Label(mainWindow, text="VIRTUAL SPEAKER", width=30, font=("Times New Roman""bold", 30), background="silver")
label_0.grid(row=3, column=5, padx=305, pady=15)

# Text Entry Label
label_2 = Label(mainWindow, text=" Type what you want me to speak for you: ", width=10,
                font=("Times New Roman""bold", 14), background="silver")
label_2.grid(row=7, column=5, ipadx=200, ipady=50)

# Text Box
entry_1 = Entry(mainWindow, font=("ariel", 24), fg="black", bg="white", textvariable=text)
entry_1.grid(row=8, column=5)

# Execution button
b1 = Button(mainWindow, text='Speak', font=("Times New Roman""bold", 14), width=20, height=2, bg='silver', fg='brown',
            command=execute)
b1.grid(row=10, column=5, padx=305, pady=15)
mainWindow.mainloop()


#################################   CONSOLE BASED PROGRAM ###########################################################

# if _name_ == '_main_':
#     print("Welcome to the Virtual Speaker 1.1 created by Vishwajeet Muthe")
#     while True:
#         x = input("Type what you want to speak: ")
#         if x == 'q':
#             break
#         command = f' mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""{x}"")(window.close)")'
#         os.system(command)