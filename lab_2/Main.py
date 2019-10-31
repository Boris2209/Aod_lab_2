from tkinter import *

from tkinter import ttk

from lab_2.CircularLinkedList import *


main_window = Tk()
main_window.title("Лаба 2, Списки сложной структуры, бинарные деревья, Литвиненко Борис, ИКБО-06-18")
main_window.geometry("1100x1000")

# create tabs
tab_control = ttk.Notebook(main_window)

""" functions and objects to perform task 1 (CircularLinkedList) """

tab_List = ttk.Frame(tab_control)
tab_control.add(tab_List, text='Кольцевой список')
tab_control.pack(expand=1, fill='both')

list_number = CircularLinkedList()

# command to input_q_button
def add_l_element():
    try:
        numb = int(input_l_element.get())
        list_number.append(numb)
        input_l_element.delete(0, END)
        l_display.configure(text=list_number.get_list())
    except Exception:
        l_display.configure(text="Неверные входные данные")


def start_l_task():
    try:
        list_number.task()
        l_display.configure(text=list_number.get_list())
    except IOError:
        l_display.configure(text="Нет элементов")
    except Exception:
        l_display.configure(text="Неверные входные данные")

# list display
l_display = Label(tab_List, text="Вводите по одному элементу", font=("Arial Bold", 20))
l_display.grid(column=0, row=0)

# input queue
input_l_element = Entry(tab_List, width=50, font=("Arial Bold", 20))
input_l_element.grid(column=0, row=1)
input_l_element.focus()

# button input
input_q_button = Button(tab_List, text="Добавить в кольцевой список", font=("Arial Bold", 15), command=add_l_element)
input_q_button.grid(column=1, row=1)

# button to task
l_button_task = Button(tab_List, text="Увеличить на 3 и убрать простые", font=("Arial Bold", 15), command=start_l_task)
l_button_task.grid(column=0, row=2)


main_window.mainloop()

