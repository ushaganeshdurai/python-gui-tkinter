import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.label = ttk.Label(root, text="Enter the desired length:")
        self.label.grid(row=0, column=0, padx=10, pady=10,)

        self.length_entry = ttk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                self.result_label.config(text="Please enter a valid positive length.")
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.result_label.config(text=f"Generated Password: {password}")

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid positive integer for the length.")

def main():
    root = tk.Tk()
    root.configure(bg="#87b7e2")
    password_generator_gui = PasswordGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
