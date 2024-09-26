import tkinter as tk

# Sample static data
data = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]

def update_results(*args):
    search_term = search_var.get().lower()
    print(search_term)
    results = [item for item in data if search_term in item]
    print(results)
    listbox.delete(0, tk.END)  # Clear the listbox
    for item in results:
        listbox.insert(tk.END, item)  # Insert matching items

# Create the main window
root = tk.Tk()
root.title("Real-Time Search")

# Variable to hold user input
search_var = tk.StringVar()
search_var.trace("w", update_results)  # Call update_results on changes

# Create and pack widgets
entry = tk.Entry(root, textvariable=search_var)
entry.pack(pady=10)

listbox = tk.Listbox()
listbox.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
