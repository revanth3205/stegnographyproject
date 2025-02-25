import cv2

img = cv2.imread("revencrypted.png",cv2.IMREAD_UNCHANGED)

try:
    with open("password.txt","r") as file:
        saved_password = file.read().strip()
except FileNotFoundError:
    print("Error: Password file not found! Ensure encryption was done first.")
    exit()

entered_password = input("enter the password for decryption:")

if entered_password == saved_password:
    c = {i: chr(i) for i in range(255)}

    message_length = int(img[0, 0, 0])

    n, m, z = 1, 1, 0

    decrypted_message = ""

    for i in range(message_length):
        pixel_value = int(img[n, m, z])
        decrypted_message += c[pixel_value]
        n += 1
        m += 1
        z = (z + 1) % 3

    print("decryption successful secret message:",decrypted_message)
else:
    print("access failed")