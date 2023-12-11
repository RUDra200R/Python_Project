from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from PIL import Image


# Function to encrypt an image using Triple-DES
def encrypt_image(image_path, key):
    # Load the image
    image = Image.open(image_path)

    # Convert the image to RGB mode if it's in a different mode
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Get the pixel data of the image
    pixel_data = image.tobytes()

    # Generate a random initialization vector (IV)
    iv = get_random_bytes(8)

    # Create a Triple-DES cipher object with the provided key and mode
    cipher = DES3.new(key, DES3.MODE_CBC, iv)

    # Pad the pixel data to make its length a multiple of 8
    padded_data = pad(pixel_data, 8)

    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)

    # Create a new image with the encrypted data
    encrypted_image = Image.frombytes(image.mode, image.size, encrypted_data)

    # Save the encrypted image
    encrypted_image.save('encrypted_image.jpg')
    print("Image encrypted successfully!")

# Provide the path to the image you want to encrypt
image_path = 'original_image.jpg'

# Provide the encryption key (must be 16 bytes long)
key = b'Sixteen byte key'

# Encrypt the image
encrypt_image(image_path, key)