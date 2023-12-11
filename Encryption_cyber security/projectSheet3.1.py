print("Welcome!")
input("Press Enter to START")
text = input("enter a word:")
shift = int(input("Enter a value for shift:"))
print("1- Encryption \n 2 - decryption")
option = (input("Choose the option: "))
if option == 'Encryption':
    def encrypt(text, shift):
        encrypt_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                encrypt_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                encrypt_text += encrypt_char
            else:
                encrypt_text += char
        return print(encrypt_text)
elif option == 'decryption':
    def decrypt(text, shift):
        decrypt_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                decrypt_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                decrypt_text += decrypt_char
            else:
                decrypt_text += char
        return print(decrypt_text)

else:
   print("Please choose valid option")
