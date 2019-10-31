from tkinter import *

from lab_2.CircularLinkedList import *

#
# # main window
# main_window = Tk()
# main_window.title("Лаба 2, Списки сложной структуры, бинарные деревья, Литвиненко Борис, ИКБО-06-18")
# main_window.geometry("1100x1000")
#
#
#
#
# main_window.mainloop()

list = CircularLinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)

print(list.get_list())

