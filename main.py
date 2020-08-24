#copyright 2020 Doggielover
from tkinter import*
from cryptography.fernet import Fernet

window = Tk()
size = 500
canvas = Canvas(window, height=size, width=size, bg="blue")
canvas.pack()
key = Fernet.generate_key()
print(key)
file = open("key.key", "wb")
file.write(key)
file.close()
Fernet = Fernet(key)
message = "what you want to encrypt goes here"
encoded = message.encode()
encrypted = Fernet.encrypt(encoded)

text = Text(window)
text.insert(INSERT, encrypted)
text.pack()
window.mainloop()
print(encrypted)