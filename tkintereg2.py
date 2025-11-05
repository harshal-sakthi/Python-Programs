import tkinter as tk
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("1000x1000")

tk.Label(root, text="Enter number 1 :", font=("Arial", 20)).pack(pady=5)
num1 = tk.Entry(root)
num1.pack()

tk.Label(root, text="Enter number 2 :", font=("Arial", 20)).pack(pady=5)
num2 = tk.Entry(root)
num2.pack()

result_label = tk.Label(root, text="Result:", font=("Arial", 20))
result_label.pack(pady=10)

def add_numbers():
    try:
        n1 = float(num1.get())
        n2 = float(num2.get())
        result = n1 + n2

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Please enter a valid number")

tk.Button(root, text="Add", command=add_numbers).pack(pady = 5)

root.mainloop()