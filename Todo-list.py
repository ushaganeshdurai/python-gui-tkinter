import tkinter as tk
from tkinter import messagebox

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.display_button = tk.Button(root, text="Display Tasks", command=self.display_tasks)
        self.display_button.grid(row=2, column=0, padx=5, pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=1, padx=5, pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def display_tasks(self):
        if not self.tasks:
            messagebox.showinfo("To-Do List", "No tasks found.")
        else:
            task_list = "\n".join(self.tasks)
            messagebox.showinfo("To-Do List", f"Tasks:\n{task_list}")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            removed_task = self.tasks.pop(index)
            self.task_listbox.delete(index)
            messagebox.showinfo("To-Do List", f"Task '{removed_task}' removed successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")


def main():
    root = tk.Tk()
    todo_list_gui = ToDoListGUI(root)
    root.configure(bg="#87b7e2")
    root.mainloop()


if __name__ == "__main__":
    main()
