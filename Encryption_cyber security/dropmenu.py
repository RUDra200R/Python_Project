import tkinter as tk


def on_selection(selection):
    print("selected option are {}".format(selection))


root = tk.Tk()
selected_option = tk.StringVar(root)
selected_option.set("option1")
dropdown = tk.OptionMenu(root, selected_option, 'option1', 'option2', 'option3')

dropdown.pack()
b2 = tk.Button(root, text='shift')
b2.pack(side='right')

root.mainloop()
