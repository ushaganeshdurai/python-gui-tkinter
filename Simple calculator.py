import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.num1_label = tk.Label(root, text="Enter number 1:")
        self.num1_label.grid(row=0, column=0, padx=10, pady=10)

        self.num1_entry = tk.Entry(root)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)

        self.num2_label = tk.Label(root, text="Enter number 2:")
        self.num2_label.grid(row=1, column=0, padx=10, pady=10)

        self.num2_entry = tk.Entry(root)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)

        self.operation_label = tk.Label(root, text="Select operation:")
        self.operation_label.grid(row=2, column=0, padx=10, pady=10)

        self.operation_var = tk.StringVar()
        self.operation_var.set("+")
        self.operation_menu = tk.OptionMenu(root, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.grid(row=2, column=1, padx=10, pady=10)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Error", "Cannot divide by zero.")
                    return
            else:
                messagebox.showerror("Error", "Invalid operation.")
                return

            messagebox.showinfo("Result", f"The result is: {result}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")


def main():
    root = tk.Tk()
    root.configure(bg="#87b7e2")
    calculator = SimpleCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
