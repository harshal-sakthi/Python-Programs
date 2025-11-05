import tkinter as tk
root = tk.Tk()
root.title("My first GUI")
root.geometry("300x200")


label = tk.Label(root, text="Hello Tkinter", font=("Arial", 14))
label.pack(pady=20)

def on_click():
    label.config(text="You clicked the button")

button = tk.Button(root, text="Click me", command=on_click)
button.pack()

root.mainloop()