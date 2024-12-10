import tkinter as tk
from tkinter import PhotoImage
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\adm\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\adm\AppData\Local\Programs\Python\Python313\tcl\tk8.6'


def add_task():
    task = entr_task.get()
    if task == "":
        return
    lbx_list.insert(tk.END, task)
    entr_task.delete(0, tk.END)


def delete_task():
    selected_task = lbx_list.curselection()
    if selected_task:
        lbx_list.delete(selected_task)


def mark_task():
    selected_task = lbx_list.curselection()
    if selected_task:
        lbx_list.itemconfig(selected_task, bg="green")
        lbx_list.selection_clear(0, tk.END)


main_window = tk.Tk()
main_window.title("Task List")
main_window.configure(bg="azure3")
main_window.minsize(300, 300)
main_window.maxsize(300, 450)

# Загрузка изображения фона
bg_image = PhotoImage(file="bg.png")

# Создание Canvas для фона и установка изображения
canvas_bg = tk.Canvas(main_window, width=300, height=450, highlightthickness=0)
canvas_bg.create_image(0, 0, anchor="nw", image=bg_image)
canvas_bg.grid(row=0, column=0, sticky="nsew")
main_window.grid_rowconfigure(0, weight=1)  # Настройка веса строки для растяжения
main_window.grid_columnconfigure(0, weight=1)  # Настройка веса столбца для растяжения

# Настройка "растяжения" canvas при изменении размеров окна
main_window.grid_rowconfigure(0, weight=1)
main_window.grid_columnconfigure(0, weight=1)

# UI элементы
lbl_task = tk.Label(main_window, text="Enter task", bg="lightblue")
lbl_task.grid(row=0, column=0, columnspan=3, pady=[10, 5])

entr_task = tk.Entry(main_window, bg="lightblue")
entr_task.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="we")

btn_add = tk.Button(main_window, text="Add task", command=add_task)
btn_add.grid(row=2, column=0, padx=10, pady=10)

btn_del = tk.Button(main_window, text="Delete task", command=delete_task)
btn_del.grid(row=2, column=1, padx=10, pady=10)

btn_mark = tk.Button(main_window, text="Mark finished task", command=mark_task)
btn_mark.grid(row=2, column=2, padx=10, pady=10)

lbl_tasks = tk.Label(main_window, text="Tasks:", bg="lightblue")
lbl_tasks.grid(row=3, columnspan=3, padx=5, pady=5)

lbx_list = tk.Listbox(main_window, width=30)
lbx_list.grid(row=4, columnspan=3, padx=10, pady=[5, 10], sticky="nswe")

main_window.mainloop()
