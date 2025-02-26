import cv2
import os

# Load the image
img = cv2.imread(r"C:\Users\balak\Downloads\stegno\mypic.jpg")  # Use absolute path

if img is None:
    print("Error: Unable to load image. Please check the file path.")
    exit(1)

# Input secret message and passcode
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Prepare dictionaries to map characters to values
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Initialize pixel positions
m, n, z = 0, 0, 0
height, width, _ = img.shape

# Encrypt the message into the image
for i in range(len(msg)):
    if n >= height:  # If we exceed image dimensions, stop encoding
        break

    pixel_value = d[msg[i]]
    img[n, m, z] = pixel_value  # Embed the message character into the image pixel

    # Move to the next pixel
    m += 1
    if m >= width:
        m = 0
        n += 1
        if n >= height:
            break

    # Move through RGB channels
    z = (z + 1) % 3

# Save the encrypted image
cv2.imwrite(r"C:\Users\balak\Downloads\stegno\encryptedImage.jpg", img)
os.system("start C:\\Users\\balak\\Downloads\\stegno\\encryptedImage.jpg")  # Open the image

# Decrypt the message
message = ""
pas = input("Enter passcode for Decryption: ")
if password == pas:
    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        pixel_value = img[n, m, z]  # Retrieve the pixel value
        message += c[pixel_value]  # Convert the pixel value back to the character

        # Move to the next pixel
        m += 1
        if m >= width:
            m = 0
            n += 1
        z = (z + 1) % 3

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
