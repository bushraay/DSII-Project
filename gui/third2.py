import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
from PIL import ImageTk 

window = tk.Tk()
window.title('My Learning Track')
window.geometry('333x500')
window['bg'] = 'maroon'
missed_tasks =[]
# # Add image file
# bg = PhotoImage(file = "My Learn Track.png")
  
# # Create Canvas
# canvas1 = Canvas( window, width = 333,
#                  height = 500)
  
# canvas1.pack(fill = "both", expand = True)

# Define the list of tasks with priority, course name, deadline date, and assignment
tasks = [
    {'priority': 3, 'course name': 'LA', 'deadline': '2023-04-23', 'Assignment': 'Final'},
    {'priority': 2, 'course name': 'CA', 'deadline': '2023-05-05', 'Assignment': 'HW'},
    {'priority': 1, 'course name': 'DSII', 'deadline': '2023-05-01', 'Assignment': 'HW'},
    {'priority': 5, 'course name': 'Hikma', 'deadline': '2023-05-01', 'Assignment': 'HW'},
    {'priority': 4, 'course name': 'IPnS', 'deadline': '2023-05-05', 'Assignment': 'HW'}
]

# Sort tasks by priority
tasks.sort(key=lambda x: x['priority'])

# Create a label widget to display the top priority task with deadline date
label = tk.Label(window, text=f"Top priority task: {tasks[0]['course name']}, Deadline: {tasks[0]['deadline']}", background='#f7d7c4')
label.pack()

# Define a function to remove the top priority task and update the label and table
def remove_top_task():
    if tasks:
        if datetime.strptime(tasks[0]['deadline'], '%Y-%m-%d').date() < datetime.now().date() :
            missed_tasks.append(tasks[0]['course name'])
        tasks.pop(0)
        
    if tasks:
        label.config(text=f"Top priority task: {tasks[0]['course name']}, Deadline: {tasks[0]['deadline']}")
        checkbox_text.set(tasks[0]['course name'])
        checkbox.deselect()
        update_table()
    else:
        label.config(text="Congratulations, No tasks left!!!")
        tree.delete(*tree.get_children())
        
    # Print missed tasks
    print(f"Missed tasks: {missed_tasks}")
    
txt_output = Text(window, height=5, width=30)
txt_output.pack(pady=30)

for item in missed_tasks:
    txt_output.insert(END, item + "\n")


# Create a Checkbutton widget for the top priority task
checkbox_text = tk.StringVar()
checkbox_text.set(tasks[0]['course name'])
checkbox = tk.Checkbutton(window, textvariable=checkbox_text, command=remove_top_task, background= "#f7d7c4")
checkbox.pack()

def update_table():
    # Clear existing items from tree
    tree.delete(*tree.get_children())
    
    # Populate tree with all tasks
    for i, task in enumerate(tasks):
        tree.insert("", "end", iid=i, values=(i+1, task['course name'], task['deadline'], task['Assignment']))
        
    # Set column widths
    tree.column("#", width=20, minwidth=20, stretch=False)
    tree.column("Course Name", width=100, minwidth=100, stretch=False)
    tree.column("Deadline", width=100, minwidth=100, stretch=False)
    tree.column("Assignment", width=80, minwidth=80, stretch=False)

# Create a table view with tasks, deadlines and assignments
tree = ttk.Treeview(window, columns=("#", "Course Name", "Deadline", "Assignment"), show="headings")
tree.heading("#", text="#")
tree.heading("Course Name", text="Course Name")
tree.heading("Deadline", text="Deadline")
tree.heading("Assignment", text="Assignment")

# Set column widths for the treeview
tree.column("#", width=50)
tree.column("Course Name", width=100)
tree.column("Deadline", width=100)
tree.column("Assignment", width=100)

# Customize the color and dimensions of the Treeview widget
style = ttk.Style(window)
style.configure("Treeview", background="#f7d7c4", foreground="black", rowheight=20, fieldbackground="#f7d7c4", font=("Calibri", 11))
style.map('Treeview', background=[('selected', '#f7d7c4')])

tree.pack(pady=20)

# Call update_table() function to populate the Treeview widget with tasks
update_table()

# Create a button to go back to the previous screen
back_button = tk.Button(window, text="Back", bg='#f7d7c4')
back_button.pack(side="bottom", pady=20)


window.mainloop()