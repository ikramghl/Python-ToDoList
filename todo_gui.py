import tkinter as tk
from tkinter import messagebox
import os

FILENAME = "tasks.txt"


LIGHT_THEME = {
    "bg": "#ffffff",
    "fg": "#000000",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000",
    "button_bg": "#e0e0e0",
    "button_fg": "#000000"
}

DARK_THEME = {
    "bg": "#2e2e2e",
    "fg": "#ffffff",
    "entry_bg": "#3c3f41",
    "entry_fg": "#ffffff",
    "button_bg": "#4a4a4a",
    "button_fg": "#ffffff"
}

current_theme = LIGHT_THEME

def apply_theme():
    root.configure(bg=current_theme["bg"])
    top_frame.configure(bg=current_theme["bg"])
    entry.configure(bg=current_theme["entry_bg"], fg=current_theme["entry_fg"], insertbackground=current_theme["fg"])
    add_button.configure(bg=current_theme["button_bg"], fg=current_theme["button_fg"])
    theme_button.configure(bg=current_theme["button_bg"], fg=current_theme["button_fg"])
    task_frame.configure(bg=current_theme["bg"])
    bottom_frame.configure(bg=current_theme["bg"])
    remove_button.configure(bg=current_theme["button_bg"], fg=current_theme["button_fg"])
    clear_button.configure(bg=current_theme["button_bg"], fg=current_theme["button_fg"])

    for widget in task_frame.winfo_children():
        if isinstance(widget, tk.Checkbutton):
            widget.configure(bg=current_theme["bg"], fg=current_theme["fg"], selectcolor=current_theme["bg"])

def toggle_theme():
    global current_theme
    if current_theme == LIGHT_THEME:
        current_theme = DARK_THEME
        theme_button.config(text="Switch to Light Mode")
    else:
        current_theme = LIGHT_THEME
        theme_button.config(text="Switch to Dark Mode")
    apply_theme()

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    tasks = []
    with open(FILENAME, "r") as file:
        for line in file:
            parts = line.strip().split("|", 1)
            if len(parts) == 2:
                var = tk.IntVar(value=int(parts[0]))
                tasks.append([var, parts[1]])
    return tasks

def save_tasks():
    with open(FILENAME, "w") as file:
        for var, desc in tasks:
            file.write(f"{var.get()}|{desc}\n")

def refresh_ui():
    for widget in task_frame.winfo_children():
        widget.destroy()
    for var, desc in tasks:
        cb = tk.Checkbutton(task_frame, text=desc, variable=var,
                            onvalue=1, offvalue=0, command=save_tasks,
                            anchor="w", width=45, padx=5,
                            bg=current_theme["bg"], fg=current_theme["fg"],
                            selectcolor=current_theme["bg"])
        cb.pack(fill="x", anchor="w")

def add_task():
    desc = entry.get().strip()
    if desc:
        var = tk.IntVar(value=0)
        tasks.append([var, desc])
        entry.delete(0, tk.END)
        save_tasks()
        refresh_ui()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty.")

def remove_completed_tasks():
    global tasks
    tasks = [task for task in tasks if task[0].get() == 0]
    save_tasks()
    refresh_ui()

def clear_all_tasks():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete ALL tasks?"):
        tasks.clear()
        save_tasks()
        refresh_ui()

# === GUI SETUP ===
root = tk.Tk()
root.title("To-Do List")

# Entry field and buttons
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

entry = tk.Entry(top_frame, width=40)
entry.pack(side=tk.LEFT, padx=(0, 10))

add_button = tk.Button(top_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

theme_button = tk.Button(top_frame, text="Switch to Dark Mode", command=toggle_theme)
theme_button.pack(side=tk.LEFT, padx=(10, 0))

# Task display area
task_frame = tk.Frame(root)
task_frame.pack(pady=10)

# Bottom buttons
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

remove_button = tk.Button(bottom_frame, text="Remove Task", command=remove_completed_tasks)
remove_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(bottom_frame, text="Clear All", command=clear_all_tasks)
clear_button.pack(side=tk.LEFT, padx=5)

# Load and display tasks
tasks = load_tasks()
refresh_ui()
apply_theme()  # apply initial theme

root.mainloop()
