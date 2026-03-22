import socket
import threading
import tkinter as tk
from tkinter import simpledialog

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("Enter server IP: ")
PORT = 12345

client.connect((ip, PORT))

# GUI
root = tk.Tk()
name = simpledialog.askstring("Name", "Enter your name:")
root.title(f"Client - {name}")

text = tk.Text(root, height=15, width=40)
text.pack()

entry = tk.Entry(root)
entry.pack()

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            text.insert(tk.END, msg + "\n")
        except:
            break

def send():
    msg = entry.get()
    if msg:
        full_msg = f"{name}: {msg}"
        client.send(full_msg.encode())
        text.insert(tk.END, "Me: " + msg + "\n")
        entry.delete(0, tk.END)

entry.bind("<Return>", lambda e: send())

tk.Button(root, text="Send", command=send).pack()

threading.Thread(target=receive, daemon=True).start()

root.mainloop()