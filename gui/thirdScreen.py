import tkinter as tk
from tkinter import ttk
from datetime import datetime


window = tk.Tk()
window.title('My Learning Track')
window.geometry('700x450')
window['bg'] = 'maroon'

# Define the list of tasks with priority and deadline date
tasks = [
    {'priority': 3, 'name': 'LA', 'deadline': '2023-04-30'},
    {'priority': 2, 'name': 'CA', 'deadline': '2023-05-05'},
    {'priority': 1, 'name': 'DSII', 'deadline': '2023-05-01'},
    {'priority': 5, 'name': 'Hikma', 'deadline': '2023-05-01'},
    {'priority': 4, 'name': 'IPnS', 'deadline': '2023-05-05'}
]

# Sort tasks by priority
tasks.sort(key=lambda x: x['priority'])

# Create a label widget to display the top priority task with deadline date
label = tk.Label(window, text=f"Top priority task: {tasks[0]['name']}, Deadline: {tasks[0]['deadline']}", background='gold')
label.pack()

# Define a function to remove the top priority task and update the label and table
def remove_top_task():
    if tasks:
        tasks.pop(0)
        
    if tasks:
        label.config(text=f"Top priority task: {tasks[0]['name']}, Deadline: {tasks[0]['deadline']}")
        checkbox_text.set(tasks[0]['name'])
        checkbox.deselect() # because in tkinter by default the box gets checked 
        update_table()
    else:
        label.config(text="Well Done, No tasks left!!!")
        tree.delete(*tree.get_children()) #deletes all the items from a tkinter treeview widget
        #tree.get_children() returns a tuple of all the items in treeview and * unpacks the tuple in individual arguments

# Create a Checkbutton widget for the top priority task
checkbox_text = tk.StringVar()
checkbox_text.set(tasks[0]['name'])
checkbox = tk.Checkbutton(window, textvariable=checkbox_text, command=remove_top_task, background= "gold")
checkbox.pack()

# Create a table view with tasks and deadlines
tree = ttk.Treeview(window, columns=("Task", "Deadline"), show="headings")
tree.heading("Task", text="Task")
tree.heading("Deadline", text="Deadline")
tree.pack()

def update_table():
    # Clear existing items from tree
    tree.delete(*tree.get_children())
    
    # Populate tree with updated tasks
    for task in tasks:
        tree.insert("", "end", values=(task['name'], task['deadline']))

update_table()

# Create a button to go back to the previous screen
back_button = tk.Button(window, text="Back", bg='gold')
back_button.pack(side="bottom", pady=20)

window.mainloop()