import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Phone Directory")
root.geometry("400x400")

# Dictionary to store contacts (Name: Phone)
contacts = {}

# Functions
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    
    if name and phone:
        contacts[name] = phone
        update_listbox()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both a Name and Phone number.")

def update_listbox():
    contact_listbox.delete(0, tk.END)
    for name, phone in contacts.items():
        contact_listbox.insert(tk.END, f"{name}: {phone}")

def delete_contact():
    try:
        selected_text = contact_listbox.get(contact_listbox.curselection())
        name = selected_text.split(":")[0].strip()
        del contacts[name]
        update_listbox()
    except:
        messagebox.showwarning("Selection Error", "Please select a contact from the list to delete.")

# UI Elements (Widgets)
tk.Label(root, text="Name:", font=("Arial", 10, "bold")).pack(pady=2)
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=2)

tk.Label(root, text="Phone:", font=("Arial", 10, "bold")).pack(pady=2)
phone_entry = tk.Entry(root, width=30)
phone_entry.pack(pady=2)

add_btn = tk.Button(root, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white", width=15)
add_btn.pack(pady=10)

contact_listbox = tk.Listbox(root, width=40, height=10)
contact_listbox.pack(pady=10)

delete_btn = tk.Button(root, text="Delete Selected", command=delete_contact, bg="#f44336", fg="white", width=15)
delete_btn.pack(pady=5)

# Start the application loop
root.mainloop()
