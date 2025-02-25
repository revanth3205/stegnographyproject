import cv2
import os

img = cv2.imread("revanthproject.jpg",cv2.IMREAD_UNCHANGED)

msg = input("enter the secret message:")
password = input("enter the passcode:")

d = {chr(i): i for i in range(255) }

img[0 ,0 ,0] = len(msg)

n, m, z = 1, 1, 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n +=1
    m +=1
    z = (z+1)%3

cv2.imwrite("revencrypted.png",img)
print("message encrypted succcessfully in 'revencrypted.png'")

with open("password.txt","w") as file:
    file.write(password)