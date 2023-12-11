import tkinter as tk


def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result


def encrypt_text():
    input_text = input_entry.get()
    shift = int(shift_var.get())
    encrypted_text = caesar_cipher(input_text, shift)
    output_text.set(encrypted_text)


def decrypt_text():
    input_text = input_entry.get()
    shift = int(shift_var.get())
    decrypted_text = caesar_cipher(input_text, -(shift))
    output_text.set(decrypted_text)


# Create the main window
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("300x200")

# Create the input text entry field
input_entry = tk.Entry(window, width=30)
input_entry.pack(pady=10)

# Create the shift drop-down option
shift_var = tk.StringVar(window)
shift_var.set("3")
shift_option = tk.OptionMenu(window, shift_var, "1", "2", "3", "4", "5")
shift_option.pack()

# Create the Encrypt button
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_text)
encrypt_button.pack(pady=10)

# Create the Decrypt button
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

# Create the output text label
output_text = tk.StringVar(window)
output_label = tk.Label(window, textvariable=output_text)
output_label.pack(pady=10)

# Start the GUI main loop
window.mainloop()
