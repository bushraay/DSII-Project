import tkinter as tk
from tkcalendar import Calendar
from tkcalendar import DateEntry

import tkinter as tk

class TodolistApp:
    def __init__(self, master):
        self.master = master
        master.title("Todolist")
        master.geometry("333x500")

        # Load the image file
        self.background_image = tk.PhotoImage(file="bg2.png")

        # Create a canvas and display the image on it
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
        self.master.after(4000, self.master.destroy)


if __name__ == '__main__':
    root = tk.Tk()
    app = TodolistApp(root)
    root.mainloop()


class TodoListApp:
    def __init__(self, master):
        self.master = master
        master.title("Todo List App")
        master.geometry("333x500")
        master.configure(bg="maroon")

        self.todo_list = []

        self.weightage_label = tk.Label(master, text="Subject", bg="maroon", fg="white")
        self.weightage_label.pack()

        self.todo_entry = tk.Entry(master, bg="white", fg="black")
        self.todo_entry.pack()

        self.weightage_label = tk.Label(master, text="Assignment", bg="maroon", fg="white")
        self.weightage_label.pack()

        self.todo_entry = tk.Entry(master, bg="white", fg="black")
        self.todo_entry.pack()

        self.weightage_label = tk.Label(master, text="Weightage", bg="maroon", fg="white")
        self.weightage_label.pack()

        self.weightage_entry = tk.Entry(master, bg="white", fg="black")
        self.weightage_entry.pack()

        self.deadline_label = tk.Label(master, text="Deadline", bg="maroon", fg="white")
        self.deadline_label.pack()

        self.deadline_entry = DateEntry(master, bg="white", date_pattern="yyyy-mm-dd")
        self.deadline_entry.pack()

        

        self.add_button = tk.Button(master, text="Add", command=self.add_todo, bg="white")
        self.add_button.pack()

        self.todo_frame = tk.Frame(master, bg="white")
        self.todo_frame.pack()

    def add_todo(self):
        todo = self.todo_entry.get()
        weightage = self.weightage_entry.get()
        deadline = self.deadline_entry.get()

        self.todo_entry.delete(0, tk.END)
        self.weightage_entry.delete(0, tk.END)
        self.deadline_entry.delete(0, tk.END)

        self.todo_list.append((todo, weightage, deadline))

        todo_label = tk.Label(self.todo_frame, text=f"{todo}, weightage: {weightage}, deadline: {deadline}", bg="white", fg="black")
        todo_label.pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
