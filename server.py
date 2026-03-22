import socket
import threading
import tkinter as tk
from tkinter import simpledialog

HOST = "0.0.0.0"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for connection...")
conn, addr = server.accept()
print("Connected to:", addr)

# GUI
root = tk.Tk()
name = simpledialog.askstring("Name", "Enter your name:")
root.title(f"Server - {name}")

text = tk.Text(root, height=15, width=40)
text.pack()

entry = tk.Entry(root)
entry.pack()

def receive():
    while True:
        try:
            msg = conn.recv(1024).decode()
            text.insert(tk.END, msg + "\n")
        except:
            break

def send():
    msg = entry.get()
    if msg:
        full_msg = f"{name}: {msg}"
        conn.send(full_msg.encode())
        text.insert(tk.END, "Me: " + msg + "\n")
        entry.delete(0, tk.END)

entry.bind("<Return>", lambda e: send())

tk.Button(root, text="Send", command=send).pack()

threading.Thread(target=receive, daemon=True).start()

root.mainloop()